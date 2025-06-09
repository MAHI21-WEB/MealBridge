from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RestaurantUserCreationForm
from .models import RestaurantUser
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template

def register(request):
    if(request.method=='POST'):
        form= RestaurantUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form= RestaurantUserCreationForm()
    return render(request, 'RestaurantUser/register.html', {'form': form})