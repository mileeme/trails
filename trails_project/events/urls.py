from django.urls import path
from . import views


# name the app for namespacing
app_name = 'events'
urlpatterns = [
    # ex: /events/
    path('', views.index, name='index'),
    # ex: /events/5
    path('<int:event_id>/', views.event, name='event'),
    # search page
    path('search/', views.search, name='search'),
    # ex: /events/organizer/5
    path('organizer/<int:organizer_id>/', views.organizer, name='organizer'),
]
