from django.db import models
from UserSetup.models import RestaurantUser

class FoodRequest(models.Model):
    FOOD_TYPES = (
        ("Veg", "Veg"),
        ("Non Veg", "Non Veg"),
    )

    req_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE)
    foodType = models.CharField(max_length=20, choices=FOOD_TYPES, default="Veg")
    ticket = models.BooleanField(default=True)
    claimed_by = models.CharField(max_length=100, null=True, blank=True, default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.restaurant.user.username} - {self.foodType}"
