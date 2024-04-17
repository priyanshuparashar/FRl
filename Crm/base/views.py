from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import ResgistartionForm
# Create your views here.

def home(request):
    
    return  render(request ,template_name="index.html")

def sign_up(request):
    if request.method=='POST':
        form = ResgistartionForm(request.POST)
        if form.is_valid:
            user=form.save()
            login(request,user)
            return HttpResponse("logged in")
    else:
        form = ResgistartionForm()
    return render(request, 'registration/sign_up.html',{'form':form})