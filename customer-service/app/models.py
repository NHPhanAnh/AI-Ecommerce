from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cart_items')
    item_id = models.IntegerField()  # ID from Laptop or Mobile service
    item_type = models.CharField(max_length=50) # 'laptop' or 'mobile'
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item_type} - {self.item_id} (Q: {self.quantity})"
