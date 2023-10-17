# from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework import permissions
# from .serializers import ItemSerializer, AbstractBaseUserSerializer, BaseUserManagerSerializer
# from .models import Item, BaseUserManager, AbstractBaseUser  

# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()  # Replace 'Item' with your actual model
#     serializer_class = ItemSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class BaseUserManagerViewSet(viewsets.ModelViewSet):
#     queryset = BaseUserManager.objects.all()  # Replace 'BaseUserManager' with your actual model
#     serializer_class = BaseUserManagerSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class AbstractBaseUserViewSet(viewsets.ModelViewSet):
#     queryset = AbstractBaseUser.objects.all()  # Replace 'AbstractBaseUser' with your actual model
#     serializer_class = AbstractBaseUserSerializer
#     permission_classes = [permissions.IsAuthenticated]

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the furniture_app home.")

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')