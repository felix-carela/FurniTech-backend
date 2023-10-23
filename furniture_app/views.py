from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponse
from rest_framework import viewsets
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserCreateSerializer, OrderSerializer, ItemSerializer
from .models import Item, Order
from django.contrib.sessions.models import Session
from django.http import JsonResponse


User = get_user_model()

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


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
        csrf_token = get_token(request)

        # Ensure the session is saved and get the session ID
        if not request.session.session_key:
            request.session.save()
        session_id = request.session.session_key

        print(f"User {user.username} created and logged in successfully!")
        response_data = {
            "username": user.username,
            "email": user.email,
            "csrfToken": csrf_token,
            "sessionId": session_id,
            "message": "User created and logged in successfully!"
        }
        return JsonResponse(response_data, status=201)

    print("Signup serializer errors:", serializer.errors)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)  
    if user:
        login(request, user)
        csrf_token = get_token(request)
        session_id = request.session.session_key
        return Response({'username': user.username, 'email': user.email, 'csrfToken': csrf_token, 'sessionId': session_id})
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    # Clear the user's session and CSRF cookie
    logout(request)
    request.session.flush()
    
    # Manually expire the cookies by setting a very short max_age
    response = HttpResponse("Logged out successfully")
    response.set_cookie('sessionid', '', max_age=1)
    response.set_cookie('csrftoken', '', max_age=1)
    
    return response

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_view(request):
    print("Delete User View Called for user:", request.user.username)
    request.user.delete()
    print(f"User {request.user.username} deleted!")
    return Response({"message": "User deleted successfully!"})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_email(request):
    print(request.data)
    user = request.user
    old_email = user.email  # Capture the old email before updating

    # Check if the 'email' field is present in the request data
    if 'email' not in request.data:
        return Response({"error": "New email is required."}, status=400)

    serializer = UserSerializer(user, data=request.data, partial=True, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        new_email = user.email  # Capture the new email after updating

        # Return a custom message indicating the success of the update
        return Response({
            "message": "Email updated successfully!",
            "new_email": new_email
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
def create_order(request):
    print("Create Order View Called")
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()  # This will create both the order and its associated order items
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['GET'])
def get_orders_by_username(request, username):
    try:
        user = get_user_model().objects.get(username=username)
        orders = Order.objects.filter(user=user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    except get_user_model().DoesNotExist:
        return Response({"error": "User with this username does not exist."}, status=404)

