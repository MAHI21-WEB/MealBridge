from django.shortcuts import render, redirect
from .models import FoodRequest
from UserSetup.models import NGOUser, RestaurantUser
from .utils import send_wa_message
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def initiate_request(request):
    if request.method=='POST':
        food_request = FoodRequest(
            req_id=None,  
            name=request.user.username,
            foodType=request.POST.get('foodType'),
            ticket=True,  
            claimed_by=None,
            date=None,  # AutoField will auto-set the date
        )

        restaurant = RestaurantUser.objects.get(user=request.user)




        ngos=NGOUser.objects.filter(city=request.POST.get('city'))

        food_request.save()

        link=request.build_absolute_uri(f'/accept_request/{food_request.req_id}/')

        for ngo in ngos:
            if ngo.is_approved:
                message= f'Greetings! \nA new food request has been initiated by {food_request.name}.\n\nCity: {restaurant.city}\nLocation: {restaurant.location_link}\nFood Type: {food_request.foodType}\nContact: {restaurant.phoneno}\n\nTo accept this request, please visit the link below:\n\n{link}\n\nThank you for your support!'
                send_wa_message(ngo.phoneno,message)
                messages.success(request, 'Food request initiated successfully! NGOs have been notified via WhatsApp.')
                
    return redirect('dashboard')




@login_required
def accept_request(request, req_id):
    try:
        food_request = FoodRequest.objects.get(req_id=req_id)
        if request.method == 'POST':
            if food_request.ticket:
                food_request.claimed_by = request.user.username
                food_request.ticket = False  # Mark as claimed
                food_request.save()
                messages.success(request, 'Food request accepted successfully!')

                restaurant = RestaurantUser.objects.get(user=request.user)
                ngo = NGOUser.objects.get(user=request.user)
                restaurant.drives_done.append({"ID": food_request.req_id,"Restaurant": food_request.name ,"NGO": food_request.claimed_by,"Date": food_request.date})
                ngo.drives_done.append({"ID": food_request.req_id,"Restaurant": food_request.name ,"NGO": food_request.claimed_by,"Date": food_request.date})
                restaurant.save()
                ngo.save()
                return redirect('dashboard')
            else:
                messages.error(request, 'This food request has already been claimed by another NGO.')
                return redirect('dashboard')
        return render(request, 'Food/accept_request.html', {'food_request': food_request})
    except FoodRequest.DoesNotExist:
        messages.error(request, 'Food request not found.')
        return redirect('dashboard')        