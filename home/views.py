import json
import uuid
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from .models import Advisor, Customer, Booking
from .serializers import AdvisorSerializer, BooKingSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from rest_framework.decorators import permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework import status
# from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from .imports import *
from .utils import *


@permission_check('User')
def home(request):
    return HttpResponse("hello")

@api_view(['POST'])
@csrf_exempt
def customerRegister(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)

        customer_name = request_data["name"]
        customer_email = request_data["email"]
        customer_password = request_data["password"]
        if not customer_name:
            return Response({"message": "name is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not customer_email:
            return Response({"message": "email is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not customer_password:
            return Response({"message": "password is required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email__iexact=customer_email).exists():
                return Response({"message":"Email id already Registered."}, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.create(username=customer_email,email=customer_email,first_name=customer_name)
        user.set_password(customer_password)
        user.save()


        customer_obj = Customer.objects.create(user_id=user,name=customer_name, email=customer_email, password=customer_password)
        return HttpResponse("Register Successful")






@api_view(['POST'])
@csrf_exempt
def customerLogIn(request):
    if request.method == "POST":
        try:
            # fetch email and password from form
            email = request.data.get("email", None)
            password = request.data.get("password", None)
            if not email:
                return Response({"message": "email is required"}, status=status.HTTP_400_BAD_REQUEST)
            if not password:
                return Response({"message": "password is required"}, status=status.HTTP_400_BAD_REQUEST)

            if not User.objects.filter(email__iexact=email).exists():
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            # Authenticate with username and password
            user = authenticate(username=User.objects.get(email=email).username, password=password)
            if user is not None:

                login(request, user)  # login user
                # If Credentials are Correct and user found
                payload = {'username': user.username}
                auth_token = encode_auth_token(payload, "login")
                refresh_token = encode_auth_token(payload, "refresh")

                data = {
                    "message": "user login Successfully.",
                    "token": auth_token,
                    "refresh_token": refresh_token,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                # if login information are invalid
                return Response({"message": "Invalid Login Credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            #print('Error: ', e)
            return Response({"message": "Something went wrong Please Try again Later."}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

@api_view(['POST'])
@csrf_exempt
@permission_check('Admin')
def createAdvisor(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)

        name = request_data["name"]
        profile_pic = request_data["profile_pic"]
        if not customer_name:
            return Response({"message": "name is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not customer_email:
            return Response({"message": "email is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not customer_password:
            return Response({"message": "password is required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email__iexact=customer_email).exists():
                return Response({"message":"Email id already Registered."}, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.create(username=customer_email,email=customer_email,first_name=customer_name)
        user.set_password(customer_password)
        user.save()


        customer_obj = Advisor.objects.create(user_id=user,name=customer_name, email=customer_email, password=customer_password)


        return HttpResponse(json_data, content_type='application/json')




@api_view(['GET'])
@permission_check('User')
def getAdvisor(request,user_id):

    adv = Advisor.objects.all()
    serializer = AdvisorSerializer(adv, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['POST','GET'])
@csrf_exempt
@permission_check('User')
def bookCall(request, user_id, advisor_id):
    user = Customer.objects.get(id=user_id)
    advisor = Advisor.objects.get(id=advisor_id)
    if request.method == 'POST':
        request_data = json.loads(request.body)
        booking_time = request_data["booking_time"]
        #print(booking_time)
        booking_object = Booking.objects.create(advisor_id=advisor,booking_id=user,booking_time=booking_time)

    return HttpResponse("Booking Save")




@api_view(['GET', 'POST'])
@permission_check('User')
def getBookingCall(request,user_id):
    print(user_id)
    bookings = Booking.objects.filter(booking_id=Customer.objects.get(id=user_id))
    serializer = BooKingSerializer(bookings, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
















