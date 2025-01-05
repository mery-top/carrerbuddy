from django.urls import path
from .import views

urlpatterns = [
    path("aibuddy/", views.AibuddyView, name='aibuddy'),
    path("aiprofile/", views.AiprofileView, name='aiprofile'),
    path("aiupdate/", views.AiupdateView, name='aiupdate'),
]