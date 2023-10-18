from django.urls import path, include
from . import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # User-related endpoints
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-user/', views.delete_user_view, name='delete-user'),
    path('update-username/', views.update_username, name='update-username'),

    # Item-related endpoints
    path('items/', views.ItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='item-list'),

    # Order-related endpoints
    path('orders/create/', views.create_order, name='order-create'),
    path('orders/user/', views.list_user_orders, name='user-orders'),
]
