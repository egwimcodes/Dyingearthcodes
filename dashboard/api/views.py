from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView, Request, Response, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import GetAllUsersSerializer, GetUserSerializer, GetAllSensorSerializer, GetAllSoldSensorQrSerializer, GetAllUnSoldSensorQrSerializer
from dashboard.models import User, Sensor, SoldSensorQr, UnSoldSensorQr
from drf_yasg.utils import swagger_auto_schema


class APIHomePage(APIView):
    @swagger_auto_schema(
        responses={
            200: 'OK',
        }
    )
    def get(self, request, *args, **kwargs):
        data = {
            'API Home': 'api/v1/home/',
            'Users': 'api/v1/users/',
            'User': 'api/v1/user/',
            'Sensors': 'api/v1/sensors/',
            'Sensor': 'api/v1/sensor/',
            'Sold Sensors Qr Code': 'api/v1/sold-sensor-qr/',
            'Unsold Sensors Qr Code': 'api/v1/unsold-sensor-qr/',
        }
        return Response(data, status=status.HTTP_200_OK)
class GetAllUsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetAllUsersSerializer    
    
class GetUserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = GetAllUsersSerializer
    lookup_field = 'pk'
    
class GetAllSensorsAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = GetAllSensorSerializer
    
    
class GetSensorAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = GetAllSensorSerializer
    lookup_field = 'pk'
    
class GetSoldSensorsQrListAPIView(ListCreateAPIView):
    queryset = SoldSensorQr.objects.all()
    serializer_class = GetAllSoldSensorQrSerializer

class GetSoldSensorQrListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SoldSensorQr.objects.all()
    serializer_class = GetAllSoldSensorQrSerializer
    lookup_field = 'pk'
    
    
class GetUnSoldSensorsQrListAPIView(ListCreateAPIView):
    queryset = UnSoldSensorQr.objects.all()
    serializer_class = GetAllUnSoldSensorQrSerializer

class GetUnSoldSensorQrListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UnSoldSensorQr.objects.all()
    serializer_class = GetAllUnSoldSensorQrSerializer
    lookup_field = 'pk'