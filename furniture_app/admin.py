from django.contrib import admin
from .models import Item  # Import the Furniture model, not FurnitureStyle

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'tags', 'category', 'image')  
    search_fields = ['name']  
admin.site.register(Item, ItemAdmin) 