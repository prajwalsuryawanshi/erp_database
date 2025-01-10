from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Users
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

# Create User View
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Attempt to create the user
                serializer.save(is_active=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View Users
@api_view(['GET'])
def view_users(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# Update User
@api_view(['PUT'])
def update_user(request, user_id):
    user = get_object_or_404(Users, user_id=user_id)
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete User
@api_view(['DELETE'])
def delete_user(request, user_id):
    user = get_object_or_404(Users, user_id=user_id)
    user.is_active = False
    user.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
