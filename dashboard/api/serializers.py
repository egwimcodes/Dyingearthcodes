from rest_framework import serializers
from ..models import User, Sensor, SoldSensorQr, UnSoldSensorQr

class GetAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'country', 'city', 'zip_code', 'avatar']
        
        
        
class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'country', 'city', 'zip_code', 'avatar']
        

class GetAllSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','user', 'name', 'location']
        
        
class GetAllSoldSensorQrSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldSensorQr
        fields = ['id', 'sensor', 'sold_sensor_qr_code']
        

class GetAllUnSoldSensorQrSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnSoldSensorQr
        fields = ['id','unsold_sensor_qr_code']