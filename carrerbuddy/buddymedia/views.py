from django.shortcuts import render, redirect
# Create your views here.

def BuddymediaView(request):
    return render(request, 'buddymedia.html')
