import django_filters
import datetime

from django import forms
from django.db.models import Q
from .models import Event, Distance
from tempus_dominus.widgets import DatePicker


# class EventFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     start = django_filters.DateFilter(lookup_expr='gte')
#     end = django_filters.DateFilter(lookup_expr='lte')
#     class Meta:
#         model = Event
#         fields = ['title', 'start', 'end', 'subcategory', 'distance']

class EventFilter(django_filters.FilterSet):
    keyword_lookup = django_filters.CharFilter(method='lookup_multi_fields', label='search by keyword')
    date = django_filters.DateFilter(
        label='start date',
        lookup_expr='gte',
        widget=DatePicker(
            options={
                'input_group': False,
                'auto-close': True,
            },
            # attrs={
            #     'class': 'form-control datetimepicker-input',
            #     'data-target': '#datetimepicker1',
            #     'autocomplete': 'off',
            #     'placeholder': datetime.date.today(),
            # },
        ),
    )
    # date_end = django_filters.DateFilter(
    #     label='start date',
    #     lookup_expr='lte',
    #     widget=DatePicker(),
    # )

    # multiple choice distances
    distance__length = django_filters.ModelMultipleChoiceFilter(
        to_field_name='length',
        queryset=Distance.objects.all(),
        lookup_expr='exact',
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Event
        fields = ('keyword_lookup', 'date', 'distance__length')
        # dictionary of field names mapped to list of lookups
        # fields = {
        #     # 'title': ['icontains'],
        #     'date': ['exact', 'range'],
        #     # 'start': ['gte'],
        #     # 'end': ['lte'],
        #     # 'subcategory': ['exact'],
        #     'distance': ['length__gte'],
        # }

    def lookup_multi_fields(self, queryset, name, value):
        return queryset.filter(
            Q(distance__length__icontains=value) | Q(title__icontains=value) | Q(city__icontains=value) | Q(distance__distance_type__icontains=value)
        )
