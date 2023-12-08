from django.urls import path
from .views import APIHomePage, GetAllUsersListAPIView, GetUserAPIView, GetAllSensorsAPIView, GetSensorAPIView, GetSoldSensorsQrListAPIView, GetSoldSensorQrListAPIView, GetUnSoldSensorsQrListAPIView, GetUnSoldSensorQrListAPIView





urlpatterns = [
    path('v1/home/', APIHomePage.as_view(), name='api-home'),
    path('v1/users/', GetAllUsersListAPIView.as_view(), name='users-list'),
    path('v1/user/<pk>/', GetUserAPIView.as_view(), name='user-list'),
    path('v1/sensors/', GetAllSensorsAPIView.as_view(), name='sensors-list'),
    path('v1/sensor/<pk>/', GetSensorAPIView.as_view(), name='sensor-list'),
    path('v1/sold-sensors-qr/', GetSoldSensorsQrListAPIView.as_view(), name='sold-sensors-qr-list'),
    path('v1/sold-sensor-qr/<pk>/', GetSoldSensorQrListAPIView.as_view(), name='sold-sensor-qr-list'),
    path('v1/unsold-sensors-qr/', GetUnSoldSensorsQrListAPIView.as_view(), name='unsold-sensors-qr-list'),
    path('v1/unsold-sensor-qr/<pk>/', GetUnSoldSensorQrListAPIView.as_view(), name='unsold-sensor-qr-list'),
]
