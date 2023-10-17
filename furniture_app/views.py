from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ItemSerializer, AbstractBaseUserSerializer, BaseUserManagerSerializer
from .models import Item, BaseUserManager, AbstractBaseUser  

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # Replace 'Item' with your actual model
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class BaseUserManagerViewSet(viewsets.ModelViewSet):
    queryset = BaseUserManager.objects.all()  # Replace 'BaseUserManager' with your actual model
    serializer_class = BaseUserManagerSerializer
    permission_classes = [permissions.IsAuthenticated]

class AbstractBaseUserViewSet(viewsets.ModelViewSet):
    queryset = AbstractBaseUser.objects.all()  # Replace 'AbstractBaseUser' with your actual model
    serializer_class = AbstractBaseUserSerializer
    permission_classes = [permissions.IsAuthenticated]
