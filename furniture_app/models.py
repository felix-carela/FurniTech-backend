from django.db import models

STYLE_CHOICES = [
    ('Lighting', 'Lighting'),
    ('Furniture', 'Furniture'),
    ('Decor', 'Decor'),
    ('Linens', 'Linens'),
]

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField('Item', related_name='orders')
    total_sales = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    order_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"
    

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    color = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)
    category = models.CharField(choices=STYLE_CHOICES, default='Furniture', max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    image = models.URLField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
