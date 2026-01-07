\from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import FoodRequest
from .serializers import FoodRequestSerializer
from UserSetup.models import NGOUser, RestaurantUser
from .utils import send_wa_message

class FoodRequestListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = FoodRequest.objects.all()
        serializer = FoodRequestSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            restaurant = RestaurantUser.objects.get(user=request.user)
        except RestaurantUser.DoesNotExist:
            return Response({"error": "Not a registered restaurant user."}, status=403)

        serializer = FoodRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant=restaurant)

            ngos = NGOUser.objects.filter(city=request.data.get('city'))
            link = request.build_absolute_uri(f"/accept_request/{serializer.data['req_id']}/")

            for ngo in ngos:
                if ngo.is_approved:
                    message = (
                        f"Greetings!\nA new food request has been initiated by {request.user.username}.\n\n"
                        f"City: {restaurant.city}\nLocation: {restaurant.location_link}\n"
                        f"Food Type: {serializer.data['foodType']}\nContact: {restaurant.phoneno}\n\n"
                        f"To accept this request, visit:\n{link}\n\nThank you!"
                    )
                    send_wa_message(ngo.phoneno, message)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AcceptFoodRequest(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, req_id):
        try:
            food_request = FoodRequest.objects.get(req_id=req_id)
        except FoodRequest.DoesNotExist:
            return Response({"error": "Food request not found."}, status=404)

        if not food_request.ticket:
            return Response({"message": "Already claimed."}, status=400)

        ngo = NGOUser.objects.get(user=request.user)
        restaurant = food_request.restaurant

        food_request.claimed_by = request.user.username
        food_request.ticket = False
        food_request.save()

        restaurant.drives_done.append({
            "ID": food_request.req_id,
            "Restaurant": restaurant.user.username,
            "NGO": ngo.user.username,
            "Date": str(food_request.date)
        })
        ngo.drives_done.append({
            "ID": food_request.req_id,
            "Restaurant": restaurant.user.username,
            "NGO": ngo.user.username,
            "Date": str(food_request.date)
        })
        restaurant.save()
        ngo.save()

        return Response({"message": "Request accepted successfully."}, status=200)
