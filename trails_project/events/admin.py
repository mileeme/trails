from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Distance, Organizer, SubCategory, EventPhoto, Event, EventDistanceM2M, SubCatEventM2M
from .forms import EventDetailForm


# Registered models
@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ('length', 'distance_type',)
    # def get_event(self, obj):
    #     return obj.event.title
    # get_event.title = 'event_title'

@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'web')

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(EventPhoto)
class EventPhotoAdmin(admin.ModelAdmin):
    list_display = ('event', 'photo',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'city', 'state',)
    filter_horizontal = ('distance',)
    form = EventDetailForm

@admin.register(EventDistanceM2M)
class EventDistanceM2MAdmin(admin.ModelAdmin):
    list_display = ('distance', 'event')

@admin.register(SubCatEventM2M)
class SubCatEventM2MAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'event')


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ('category', 'name',)
#
# @admin.register(Organizer)
# class OrganizerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'web', 'email', 'area_code', 'phone',)
#
# @admin.register(Venue)
# class VenueAdmin(admin.ModelAdmin):
#     list_display = ('name', 'city', 'state',)

# @admin.register(EventDistanceM2M)
# class EventDistanceAdmin(admin.ModelAdmin):
#     list_display = ('event', 'distance')

# @admin.register(SubCatEventM2M)
# class SubCatEventM2MAdmin(admin.ModelAdmin):
#     list_display = ('subcategory', 'event',)
#
# @admin.register(EventDistanceM2M)
# class EventDistanceM2MAdmin(admin.ModelAdmin):
#     list_display = ('distance', 'event',)
#
# @admin.register(DistanceDetail)
# class DistanceDetailAdmin(admin.ModelAdmin):
#     lsit_display = ('event', 'distance', 'total_capacity',)
# # @admin.register(Participant)
# # class ParticipantAdmin(admin.ModelAdmin):
# #     list_display = ('first_name', 'last_name', 'gender', 'email')
#
# @admin.register(Registration)
# class RegistrationAdmin(admin.ModelAdmin):
#     # distance = Distance.objects.get('length')
#     # distance_type = Distance.objects.get('distance_type')
#     list_display = ('distance_detail', 'date', 'price',)
