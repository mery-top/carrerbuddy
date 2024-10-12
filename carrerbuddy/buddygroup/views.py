from django.shortcuts import render, redirect
# Create your views here.

def BuddygroupView(request):
    return render(request, 'buddygroups.html')
