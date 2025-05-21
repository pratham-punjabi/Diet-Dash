from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import AdminUser, User, Meal
from .serializers import AdminUserSerializer, UserSerializer, MealSerializer
import logging

# Generate JWT Token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def login_view(request):
    return Response({"message": "Login successful"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register_view(request):
    return Response({"message": "Register successful"})

# 🔹 Admin Signup
@api_view(['POST'])
def admin_signup(request):
    data = request.data.copy()  # Create a mutable copy
    data['password_hash'] = make_password(data.get('password'))  # Hash password
    serializer = AdminUserSerializer(data=data)

    if serializer.is_valid():
        admin = serializer.save()
        tokens = get_tokens_for_user(admin)
        return Response({"message": "Admin registered successfully", "tokens": tokens}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 🔹 Admin Login with JWT
@api_view(['POST'])
def admin_login(request):
    data = request.data
    admin = AdminUser.objects.filter(email=data.get('email')).first()

    if admin and check_password(data.get('password'), admin.password_hash):
        tokens = get_tokens_for_user(admin)
        return Response({"message": "Login successful", "tokens": tokens}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# 🔹 User Signup
@api_view(['POST'])
def user_signup(request):
    data = request.data.copy()
    data['password_hash'] = make_password(data.get('password'))
    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        return Response({"message": "User registered successfully", "tokens": tokens}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 🔹 User Login with JWT
@api_view(['POST'])
def user_login(request):
    data = request.data
    user = User.objects.filter(email=data.get('email')).first()

    if user and check_password(data.get('password'), user.password_hash):
        tokens = get_tokens_for_user(user)
        return Response({"message": "Login successful", "tokens": tokens}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# 🔹 Add Meal (Admin Only)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_meal(request):
    if not hasattr(request.user, 'is_admin') or not request.user.is_admin:
        return Response({"error": "You are not authorized to add meals"}, status=status.HTTP_403_FORBIDDEN)

    serializer = MealSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Meal added successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 🔹 Get All Meals (Any Authenticated User)
logger = logging.getLogger(__name__)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_meals(request):
    logger.info(f"Request received: {request.method} {request.path}")
    meals = Meal.objects.all()
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 🔹 Update Meal (Admin Only)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_meal(request, meal_id):
    if not hasattr(request.user, 'is_admin') or not request.user.is_admin:
        return Response({"error": "You are not authorized to update meals"}, status=status.HTTP_403_FORBIDDEN)

    meal = get_object_or_404(Meal, id=meal_id)
    serializer = MealSerializer(meal, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Meal updated successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 🔹 Delete Meal (Admin Only)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_meal(request, meal_id):
    if not hasattr(request.user, 'is_admin') or not request.user.is_admin:
        return Response({"error": "You are not authorized to delete meals"}, status=status.HTTP_403_FORBIDDEN)

    meal = get_object_or_404(Meal, id=meal_id)
    meal.delete()
    return Response({"message": "Meal deleted successfully"}, status=status.HTTP_200_OK)
