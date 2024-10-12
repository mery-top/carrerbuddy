from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ProfileForm
# Create your views here.

def AiprofileView(request):
    submitted = False
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/aiprofile?submitted=True')
    else:    
        form = ProfileForm()
            
    if 'submitted' in request.GET:
        submitted = True
        
    return render(request, 'aiprofile.html', {'form':form, 'submitted':submitted})

def AibuddyView(request):
    return render(request, 'aibuddy.html')

def AiupdateView(request):
    return render(request, 'aiupdate.html')
