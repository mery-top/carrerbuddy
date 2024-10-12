from django.urls import path
from .import views

urlpatterns = [
    path("buddymedia/", views.BuddymediaView, name='buddymedia'),
]