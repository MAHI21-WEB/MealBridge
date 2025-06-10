from django import forms

class FoodRequestCreationForm:
    foodType=forms.ChoiceField(widget=forms.RadioSelect, choices=["Veg","Non Veg"])
