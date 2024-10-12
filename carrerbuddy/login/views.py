from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

@login_required
def home(request):
    return render(request, 'home.html')
    
def SignupView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user_data_has_error = False
        
        if User.objects.filter(username=username).exists():
             user_data_has_error = True
             messages.error(request, "Username Already exists")
             
        if User.objects.filter(email=email).exists():
             user_data_has_error = True
             messages.error(request, "Email Already exists")
             
        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, "Password must be atleast 5 characters")
            
        if user_data_has_error:
            return redirect('signup')
        else:
            new_user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            messages.success(request, 'Account Created. Login now')
            return redirect('login')
        
    return render(request, 'signup.html')
    
def LoginView(request):
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('home')
        else:
            messages.error(request, "Invalid Login credentials")
            return redirect('login')
    
    
    return render(request, 'login.html')


def LogoutView(request):
    
    logout(request)
    return redirect('login')
    

