from django.contrib.auth.models import Item
from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'color', 'tags', 'category', 'image']