from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Event
from .forms import Organizer

# django's abstration template view
class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        """ return list by earliest date """
        return Event.objects.order_by('start')


# django's abstraction for displaying a list of objects
class SearchResultsView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        """ return list by earliest date """
        return Event.objects.order_by('start')
    # event = Event.objects.all()
    # context = {
    #     'event': event
    # }
    # return render(request, 'events/index.html', context)

# display a detail page for a particular type of object
class EventView(generic.DetailView):
    # generic view knows what model it will act upon via model
    # captures 'pk' from URL
    model = Event
    # by default, DetailView uses a template <app name>/<model name>_detail.html so to override, we use 'template_name' attribute to tell django to use this specific template
    template_name = 'events/event.html'
# get event details or 404 using django helper function
# we use the helper function b/c it is a design goal to maintain loose coupling
# def event(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     return render(request, 'events/event.html', {'event':event})


# for adding photo in form.py
# http://gregblogs.com/django-saving-an-image-using-imagefield-explain-a-little/
# def add_organizer_photo(request):
#     submitted = False
#     if request.method == 'POST':
#         form = OrganizerForm(requst.POST)
#         if form.is_valid():
#             orgPhoto = Pic(organizer_photo = request.FILES['organizer_photo'])
#             orgPhoto.save()
#
# def add_event_photo(request):
#     submitted = False
#     if request.method == 'POST':
#         form = EventForm(requst.POST)
#         if form.is_valid():
#             eventPhoto = Pic(event_photo = request.FILES['event_photo'])
#             eventPhoto.save()
