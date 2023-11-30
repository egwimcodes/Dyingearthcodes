from django.urls import path
from .views import APIHomePage, GetAllUsersListAPIView, GetUserAPIView


urlpatterns = [
    path('v1/home/', APIHomePage.as_view(), name='api-home'),
    path('v1/users/', GetAllUsersListAPIView.as_view(), name='users-list'),
    path('v1/user/<int:user_id>/', GetUserAPIView.as_view(), name='user-list'),
    #path('v1/sensors/', SensorListAPIView.as_view(), name='sensor-list'),
    #path('v1/sold-sensor-qr/', SoldSensorQrListAPIView.as_view(), name='sold-sensor-qr-list'),
   # path('v1/register-new-sensor/', RegisterNewSensorAPIView.as_view(), name='register-new-sensor'),
   # path('v1/update-sensor/<int:pk>/', UpdateSensorAPIView.as_view(), name='update-sensor'),
]
