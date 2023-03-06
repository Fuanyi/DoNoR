
from django.urls import path
from django.contrib import admin
from .views import UserDetailAPI, RegisterUserAPIView, DonorAPIView, PatientAPIView, BGAPIView, PatientRetreiveDestroyAPIView, DonorRetreiveDestroyAPIView
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
  path('admin', admin.site.urls),
  path('get-details', UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('token', TokenObtainPairView.as_view(), name = "token-obtain-pair"),
  path('token/refresh', TokenRefreshView.as_view(), name = "token-refresh"),
  path('login', views.UserLogIn.as_view(), name = "login"),
  path('latestDonor', views.LatestDonor.as_view()),
  path('donorList', DonorAPIView.as_view(), name="donor_list"),
  path('patientList', PatientAPIView.as_view(), name="patient_list"),
  path('BGList', BGAPIView.as_view(), name="bloodgroup_list"),
  path('patientList/<pk>', PatientRetreiveDestroyAPIView.as_view(), name="patient_single"),
  path('DonorList/<pk>', DonorRetreiveDestroyAPIView.as_view(), name="donor_single"),
]