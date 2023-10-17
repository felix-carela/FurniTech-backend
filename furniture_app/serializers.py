from rest_framework import serializers
from .models import Item, AbstractBaseUser, BaseUserManager

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class AbstractBaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractBaseUser
        fields = '__all__'

class BaseUserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUserManager
        fields = '__all__'