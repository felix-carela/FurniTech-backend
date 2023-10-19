from django.db import models

STYLE_CHOICES = [
    ('Lighting', 'Lighting'),
    ('Furniture', 'Furniture'),
    ('Decor', 'Decor'),
    ('Linens', 'Linens'),
]


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} (x{self.quantity}) for Order {self.order.order_id}"


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='orders')
    order_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"

    @property
    def total(self):
        total_cost = 0
        for order_item in self.order_items.all():
            total_cost += order_item.item.price * order_item.quantity
        return total_cost

    

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
