from django.contrib import admin
from django.core.mail import send_mail
from .models import RestaurantUser, NGOUser

@admin.register(RestaurantUser)
class RestaurantUserAdmin(admin.ModelAdmin):
    list_display=['username', 'email', 'is_approved']
    def save_model(self, request, obj, form, change):
        if change:
         old_obj=RestaurantUser.objects.get(pk=obj.pk)
         if  old_obj.is_approved==False and obj.is_approved==True:
            if obj.is_approved:
                send_mail(
                   subject='Congratulations {obj.username}! Your Restaurant Account is Approved',
                   message='Dear {obj.username},\n\nYour restaurant account has been approved. You can now log in and start using the platform.\n\nBest regards,\nMealBridge',
                   from_email= 'xyz@gmail.com',
                     recipient_list=[obj.email],
                )
        super().save_model(request, obj, form, change)
