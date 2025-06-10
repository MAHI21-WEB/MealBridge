from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RestaurantUserCreationForm, NGOUserCreationForm
from .models import RestaurantUser, NGOUser
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template

def register_restaurant(request):
    if request.method=='POST' :
        form= RestaurantUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.succes(request, 'Your account has been created successfully. You shall recieve your confirmation mail shortly')
            return redirect('login')
    else:
        form= RestaurantUserCreationForm()
    return render(request, '**register_restaurant.html', {'form': form})

def register_ngo(request):
    if request.method=='POST' :
        form= NGOUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.succes(request, 'Your account has been created successfully. You shall recieve your confirmation mail shortly')
            return redirect('login')

    else:
        form= RestaurantUserCreationForm()
    return render(request, '**register_ngo.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_aproved:
                    login(request, user)
                    return redirect('ngodashboard' if user.__class__.__name__ == 'NGOUser' else 'restaurantdashboard')
                else:
                    messages.error(request, 'Your account is not approved yet. Please wait for approval.')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Please enter both username and password')
    return render(request, '**login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')


#dashboard view up here
