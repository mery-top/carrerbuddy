from django.shortcuts import render, redirect
# Create your views here.

def MeetupView(request):
    return render(request, 'meetup.html')

def StudycallView(request):
    return render(request, 'studyroom.html', {'name': request.user.username})

