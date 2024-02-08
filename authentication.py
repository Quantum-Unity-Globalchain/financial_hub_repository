from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from api.serializers import UserSerializer  # Adjusted for directory structure

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['POST'])
def register_user(request):
    """
    Register a new user.
    """
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if not username or not email or not password:
        return JsonResponse({'error': 'Please provide all required fields.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    return JsonResponse({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    """
    Authenticate and login a user.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return JsonResponse({'token': token}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_user(request):
    """
    Logout a user.
    """
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
