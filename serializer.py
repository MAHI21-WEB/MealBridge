from rest_framework import serializers
from .models import FoodRequest

class FoodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = '__all__'
