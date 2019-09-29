from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Event
from .forms import Organizer


def index(request):
    event = Event.objects.all()
    context = {
        'event': event
    }
    return render(request, 'events/index.html', context)
# on index page, get list of events ordered by earliest start date
# class IndexView(generic.ListView):
#     template_name = 'events/index.html'
#     def get_queryset(self):
#         return Event.objects.order_by('start')

# get event details or 404 using django helper function
# we use the helper function b/c it is a design goal to maintain loose coupling
def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event.html', {'event':event})


# http://gregblogs.com/django-saving-an-image-using-imagefield-explain-a-little/
def add_organizer_photo(request):
    submitted = False
    if request.method == 'POST':
        form = OrganizerForm(requst.POST)
        if form.is_valid():
            orgPhoto = Pic(organizer_photo = request.FILES['organizer_photo'])
            orgPhoto.save()

def add_event_photo(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(requst.POST)
        if form.is_valid():
            eventPhoto = Pic(event_photo = request.FILES['event_photo'])
            eventPhoto.save()
