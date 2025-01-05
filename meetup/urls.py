from django.urls import path
from .import views

urlpatterns = [
    path("meetup/", views.MeetupView, name='meetup'),
    path("studycall/", views.StudycallView, name='studycall')
]