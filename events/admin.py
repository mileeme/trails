from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Distance, Organizer, SubCategory, EventPhoto, Event, EventDistanceM2M, SubCatEventM2M
from .forms import EventDetailForm


# Registered models
@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ('length', 'distance_type',)

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
