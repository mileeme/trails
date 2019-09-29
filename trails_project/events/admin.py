from django.contrib import admin
from .models import Category, SubCategory, Organizer, Participant, Event, Categorization, Venue, Distance, Registration
from .forms import EventDescriptionForm

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')

@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'web', 'email', 'area_code', 'phone')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'start', 'end', 'venue')
    form = EventDescriptionForm

@admin.register(Categorization)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'event')

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')

@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ('get_event', 'length', 'distance_type', 'total_capacity')
    def get_event(self, obj):
        return obj.event.title
    get_event.title = 'event_title'

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('date',)
