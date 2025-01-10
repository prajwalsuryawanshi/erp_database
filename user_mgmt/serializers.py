from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'username', 'name', 'qualification', 'email', 'contact', 'address', 'user_type', 'is_active']
