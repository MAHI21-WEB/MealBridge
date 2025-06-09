from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RestaurantUser, NGOUser

class RestaurantUserCreationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    city= forms.CharField(max_length=100, required=True)
    pincode= forms.CharField(max_length=10, required=True)
    location_link= forms.URLField(required=True)
    fssai_certification= forms.FileField(required=True)
    phoneno= forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
    
    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.is_approved = False
        if commit:
            user.save()
            RestaurantUser.objects.create(
                user=user,
                city=self.cleaned_data['city'],
                pincode=self.cleaned_data['pincode'],
                location_link=self.cleaned_data['location_link'],
                fssai_certification=self.cleaned_data['fssai_certification'],
                phoneno=self.cleaned_data['phoneno']
            )

        return user
    

class NGOUserCreationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    city= forms.CharField(max_length=100, required=True)
    pincode= forms.CharField(max_length=10, required=True)
    location_link= forms.URLField(required=True)
    certification= forms.FileField(required=True)
    phoneno= forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.is_approved = False
        if commit:
            user.save()
            NGOUser.objects.create(
                user=user,
                city=self.cleaned_data['city'],
                pincode=self.cleaned_data['pincode'],
                location_link=self.cleaned_data['location_link'],
                certification=self.cleaned_data['certification'],
                phoneno=self.cleaned_data['phoneno']
            )
        return user