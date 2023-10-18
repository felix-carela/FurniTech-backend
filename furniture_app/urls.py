from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-user/', views.delete_user_view, name='delete-user'),
    path('items/', views.ItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='item-list'),
    path('items/create/', views.create_item, name='item-create'),
    path('items/update/<int:pk>/', views.update_item, name='item-update'),
    path('items/delete/<int:pk>/', views.delete_item, name='item-delete')
   
]
