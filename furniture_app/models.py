
from django.db import models

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
    image = models.ImageField(upload_to='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
