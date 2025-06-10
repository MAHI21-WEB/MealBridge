from django.db import models
from UserSetup.models import RestaurantUser

class FoodRequest(models.Model):
    req_id=models.AutoField(primary_key=True)
    name=RestaurantUser.username
    foodType=models.CharField(choices=["Veg","Non Veg"], default="Veg")
    #city=RestaurantUser.city
    #location_link=RestaurantUser.location_link
    #phoneno=RestaurantUser.phoneno
    ticket=models.BooleanField(default=True)
    claimed_by=models.CharField(max_length=100, null=True, blank=True,default=None)
    date=models.DateTimeField(auto_now_add=True)
