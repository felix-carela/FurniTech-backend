# from django.contrib.auth.models import Item
# from rest_framework import serializers

# class ItemSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']