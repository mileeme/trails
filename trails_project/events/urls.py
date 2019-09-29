from django.urls import path
from . import views

# name the app for namespacing
app_name = 'events'
urlpatterns = [
    # ex: /events/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /events/5
    path('<int:pk>/', views.EventView.as_view(), name='event'),
]
