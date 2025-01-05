from django.urls import path
from .import views

urlpatterns = [
    path("buddygroup/", views.BuddygroupView, name='buddygroup'),
]