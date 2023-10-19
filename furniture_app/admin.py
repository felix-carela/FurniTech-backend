from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Item
from .models import Order, OrderItem

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'tags', 'category', 'price', 'image')
    search_fields = ['name']


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'display_total')
    inlines = [OrderItemInline]
    readonly_fields = ('display_total',)

    def display_total(self, obj):
        return obj.total
    display_total.short_description = 'Total'


# Unregister the default User admin and then register the User model with the custom admin
admin.site.register(Item, ItemAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Order, OrderAdmin)
