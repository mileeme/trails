from django import forms
from django.forms import ModelForm
from .models import Organizer, Event

class OrganizerForm(ModelForm):
    organizer_photo = forms.ImageField(label = 'upload your profile photo',)

class EventForm(ModelForm):
    event_photo = forms.ImageField(label = 'upload your event photo',)

class EventDescriptionForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        fields = '__all__'
        model = Event
