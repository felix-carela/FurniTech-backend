from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import JSONField



STYLE_CHOICES = [
    ('Lighting', 'Lighting'),
    ('Furniture', 'Furniture'),
    ('Decor', 'Decor'),
    ('Linens', 'Linens'),
]


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    color = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)
    category = models.CharField(choices=STYLE_CHOICES, default='Furniture', max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Order(models.Model):
    order_details = JSONField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order ID: {self.id} | User: {self.order_details.get('user_id')} | Total: {self.total}"
