from django.urls import include, path
from rest_framework import routers
from furniture_app import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('furniture_app.urls')), 
]
