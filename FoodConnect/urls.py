from django.urls import path
from .views import FoodRequestListCreate, AcceptFoodRequest

urlpatterns = [
    path('api/food-requests/', FoodRequestListCreate.as_view(), name='food-request-list-create'),
    path('api/food-requests/<int:req_id>/accept/', AcceptFoodRequest.as_view(), name='food-request-accept'),
]
