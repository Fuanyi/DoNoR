from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import UserSerializer,RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from healthApp.models import *
from healthApp.serializers import *
from rest_framework.parsers import JSONParser

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request, *args, **kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer



class DonorAPIView(generics.ListCreateAPIView):
  queryset = Donor.objects.all()
  serializer_class = DonorSerializer

class PatientAPIView(generics.ListCreateAPIView):
  queryset = Patient.objects.all()
  serializer_class = PatientSerializer

class BGAPIView(generics.ListAPIView):
  queryset = BG.objects.all()
  serializer_class = BGSerializer

class PatientRetreiveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Patient.objects.all() 
  serializer_class = PatientSerializer

class DonorRetreiveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Donor.objects.all() 
  serializer_class = DonorSerializer

class UserLogIn(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = LoginSerializer(data = request.data, context = {'request': request})
    serializer.is_valid(raise_exception = True)
    user = serializer.validated_data['user']
    token = Token.objects.get(user=user)
    return Response({
      'token':token.key,
      'id':user.pk,
      'username':user.username
    })



# class LoginView(APIView):
#     def post(self, request):
#       username = request.data.get('username')
#       password = request.data.get('password')

#       user = authenticate(username=username, password=password)

#       if user is not None:
#         response = {
#           "message": "Login successful",
#           "token": user.auth_token.key
#         }
#         return Response(data=response, status = status.HTTP_200_OK)
#       else:
#         return Response(data={"message": "Invalid  or password"})

#     def get(self, request):
#       content = {"user":str(request.user), "auth":str(request.auth)}

#       return Response(data=content, status=status.HTTP_200_OK)



class LatestDonor(APIView):
  def get(self, request, format=None):
    donor = Donor.objects.all()[0:2]
    serializer = DonorSerializer(donor, many = True)
    return Response(serializer.data)
  
