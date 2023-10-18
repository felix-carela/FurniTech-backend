from django.contrib.auth import get_user_model, login, logout, authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserCreateSerializer, OrderSerializer, ItemSerializer
from .models import Item, Order

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def signup_view(request):
    print("Signup View Called")
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)  # Log the user in after successful registration
        print(f"User {user.username} created and logged in successfully!")
        return Response({"message": "User created and logged in successfully!"}, status=201)
    print("Signup serializer errors:", serializer.errors)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_view(request):
    print("Login View Called")
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)  # Pass request to authenticate
    if user:
        login(request, user)
        print(f"User {user.username} logged in successfully!")
        return Response({"message": "Logged in successfully!"})
    print(f"Invalid credentials for username: {username}")
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    print("Logout View Called")
    logout(request)
    print("User logged out!")
    return Response({"message": "Logged out successfully!"})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_view(request):
    print("Delete User View Called for user:", request.user.username)
    request.user.delete()
    print(f"User {request.user.username} deleted!")
    return Response({"message": "User deleted successfully!"})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_username(request):
    print(request.data)
    user = request.user
    old_username = user.username  # Capture the old username before updating

    # Check if the 'username' field is present in the request data
    if 'username' not in request.data:
        return Response({"error": "New username is required."}, status=400)

    serializer = UserSerializer(user, data=request.data, partial=True, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        new_username = user.username  # Capture the new username after updating

        # Return a custom message indicating the success of the update
        return Response({
            "message": "Username updated successfully!",
            "new_username": new_username
        })
    return Response(serializer.errors, status=400)



class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_orders(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
