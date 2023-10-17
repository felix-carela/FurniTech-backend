from django.contrib import admin
from .models import Item, CustomUser, Order
from django.contrib.auth.admin import UserAdmin


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'tags', 'category', 'price', 'image')
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


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_from_order_details', 'get_item_ids_from_order_details', 'total')
    list_filter = ('order_details',)
    search_fields = ('id',)

    def get_user_from_order_details(self, obj):
        return obj.order_details.get('user_id')
    
    get_user_from_order_details.short_description = 'User ID'

    def get_item_ids_from_order_details(self, obj):
        return ", ".join(str(item_id) for item_id in obj.order_details.get('item_ids', []))
    
    get_item_ids_from_order_details.short_description = 'Item IDs'


admin.site.register(Order, OrderAdmin)
