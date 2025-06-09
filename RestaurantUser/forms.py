from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RestaurantUserCreationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    city= forms.CharField(max_length=100, required=True)
    pincode= forms.CharField(max_length=10, required=True)
    location_link= forms.URLField(required=True)
    fssai_certification= forms.FileField(required=True)
    phoneno= forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()
            from .models import RestaurantUser
            RestaurantUser.objects.create(
                user=user,
                city=self.cleaned_data['city'],
                pincode=self.cleaned_data['pincode'],
                location_link=self.cleaned_data['location_link'],
                fssai_certification=self.cleaned_data['fssai_certification'],
                phoneno=self.cleaned_data['phoneno']
            )

        return user