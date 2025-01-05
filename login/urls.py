from django.urls import path
from .import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path('signup/', views.SignupView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
]