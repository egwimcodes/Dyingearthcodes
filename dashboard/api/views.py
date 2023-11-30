from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView, Request, Response, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import GetAllUsersSerializer, GetUserSerializer
from dashboard.models import User

class APIHomePage(APIView):
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
    lookup_field = 'user_id'