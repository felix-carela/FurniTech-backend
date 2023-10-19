from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Item, Order
from .models import Item, Order, OrderItem

User = get_user_model()

# serializers.py

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)  # Add this field

    class Meta:
        model = Order
        fields = ['order_id', 'username', 'order_items']

    def validate_username(self, value):
        """
        Check that the username exists.
        """
        try:
            user = get_user_model().objects.get(username=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
        extra_kwargs = {
            'username': {'required': True},  # Ensure that the username is required for updates
        }

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name', 'description', 'color', 'tags', 'category', 'price', 'image']
