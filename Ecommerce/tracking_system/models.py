from django.db import models
from products.models import Product
 
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('shipped', 'Shipped'),
        ('canceled', 'Canceled'),
    ]

    products = models.ManyToManyField(Product, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Order {self.id}'
    
    class Meta:
        verbose_name = 'Order'
        ordering = ['-created_at']
