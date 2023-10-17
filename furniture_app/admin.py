from django.contrib import admin
from .models import Item,CustomUser
from django.contrib.auth.admin import UserAdmin
  

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'tags', 'category','price', 'image')  
    search_fields = ['name']  
admin.site.register(Item, ItemAdmin) 

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')

    
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)