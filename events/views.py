import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Event, EventPhoto, Organizer
from .filters import EventFilter
# from .forms import Organizer

# events queryset dynamic filter
def index(request):
    event_list = Event.objects.filter(date__gte=datetime.date.today()).order_by('date')[:8]
    event_filter = EventFilter(request.GET, queryset=event_list)
    template_name = 'events/index.html'
    return render(request, template_name, {'filter': event_filter})

# django's queryset dynamic filter
def search(request):
    event_list = Event.objects.all().distinct().order_by('date')
    event_filter = EventFilter(request.GET, queryset=event_list)
    template_name = 'events/search.html'
    return render(request, template_name, {'filter': event_filter})

# queryset for event page
def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    photo = EventPhoto.objects.filter(event_id=event_id)
    subcategory = event.subcategory.all()
    weekday = event.date.strftime('%A')
    similar = []
    template_name = 'events/event.html'
    context = {
        'event': event,
        'photo': photo,
        'subcategory': subcategory,
        'similar': similar,
        'weekday': weekday
    }
    return render(request, template_name, context)

# queryset for organizer page
def organizer(request, organizer_id):
    organizer = get_object_or_404(Organizer, pk=organizer_id)
    event = Event.objects.filter(organizer_id=organizer).filter(date__gte=datetime.date.today()).order_by('date')
    past = Event.objects.filter(organizer_id=organizer).filter(date__lt=datetime.date.today())
    template_name = 'events/organizer.html'
    context = {
        'organizer': organizer,
        'event': event,
        'past': past,
    }
    return render(request, template_name, context)
