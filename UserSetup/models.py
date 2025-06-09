from django.db import models
from django.contrib.auth.models import User

class RestaurantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    location_link = models.URLField()
    fssai_certification = models.FileField(upload_to='certifications/restaurant/')
    phoneno = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class NGOUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    location_link = models.URLField()
    certification = models.FileField(upload_to='certifications/ngo/')
    phoneno = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username