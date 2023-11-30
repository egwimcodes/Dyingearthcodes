from rest_framework import serializers
from ..models import User

class GetAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'country', 'city', 'zip_code', 'avatar']
        
        
        
class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'country', 'city', 'zip_code', 'avatar']