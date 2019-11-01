import django_filters
import itertools
import datetime

from django import forms
from django.db.models import Q
from .models import Event, Distance, SubCategory
from tempus_dominus.widgets import DatePicker


class EventFilter(django_filters.FilterSet):
    # keyword_lookup = django_filters.CharFilter(method='lookup_multi_fields', label='search by keyword')

    # search multiple model fields of queryset via single input field
    ex = django_filters.CharFilter(label='ex filter', method='filter_ex')
    search_fields = ['title', 'distance__length', 'subcategory__name', 'city',]

    def filter_ex(self, qs, name, value):
        if value:
            # splits string into lists of chars using whitespace
            q_parts = value.split()

            # global q_totals
            # uses Django Q object to combine using AND(&) all individual q_part objects and uses OR(|) the individual combos of field names/values
            # q_totals = Q(title__icontains='value') & Q(distance__icontains='value') | Q(...) & Q(...)
            q_totals = Q()

            # get all possible segmentations of query parts and put into possibilities list
            combinatorics = itertools.product([True, False], repeat=len(q_parts)-1)
            possibilities = []
            for combination in combinatorics:
                i = 0
                one_such_combination = [q_parts[i]]
                for slab in combination:
                    i += 1
                    if not slab:
                        one_such_combination[-1] += ' ' + q_parts[i]
                    else:
                        one_such_combination += [q_parts[i]]
                possibilities.append(one_such_combination)

            for p in possibilities:
                # stores list of fields
                list1=self.search_fields
                # stores list of user input chars
                list2=p
                # generates all possible combinations between q_parts and search_fields
                # itertools.permutations(list1, len(list2)) will generate all permutations of list1 that have length=list2
                # zip will combine elements of each tuples with elements of list2
                # ie, ('title', 'distance') and matches it up with [('title': value), ('distance': value)]
                perms = [zip(x, list2) for x in itertools.permutations(list1, len(list2))]

                for perm in perms:
                    q_part = Q()
                    for p in perm:
                        q_part = q_part & Q(**{p[0]+'__icontains':p[1]})
                    q_totals = q_totals | q_part

            qs = qs.filter(q_totals)
        return qs


    start = django_filters.DateFilter(
        field_name='date',
        label='start date',
        lookup_expr='gte',
        widget=DatePicker(
            options={
                'input_group': False,
                'auto-close': True,
            },
        ),
    )

    end = django_filters.DateFilter(
        field_name='date',
        label='end date',
        lookup_expr='lte',
        widget=DatePicker(
            options={
                'input_group': False,
                'auto-close': True,
            },
        ),
    )

    # multiple choice distances
    distance__length = django_filters.ModelMultipleChoiceFilter(
        to_field_name='length',
        queryset=Distance.objects.all(),
        lookup_expr='exact',
        widget=forms.CheckboxSelectMultiple
    )

    # multiple choice subcategory
    subcategory__name = django_filters.ModelMultipleChoiceFilter(
        to_field_name='name',
        queryset=SubCategory.objects.all(),
        lookup_expr='exact',
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = Event
        fields = ['ex', 'start', 'end', 'distance__length', 'subcategory__name',]


    # to query multiple fields in model
    # def lookup_multi_fields(self, queryset, name, value):
    #     return queryset.filter(
    #         Q(title__icontains=value) | Q(city__icontains=value) | Q(distance__length__icontains=value), Q(distance__distance_type__icontains=value)
    #     )

# class EventFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     start = django_filters.DateFilter(lookup_expr='gte')
#     end = django_filters.DateFilter(lookup_expr='lte')
#     class Meta:
#         model = Event
#         fields = ['title', 'start', 'end', 'subcategory', 'distance']
