from django.db import models

from authenticate.models import UserProfile
from tech_ecommerce.models import ProductChilds

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='order')
    total_price = models.FloatField(default=0, blank=True)
    order_count = models.IntegerField(default=0, blank=True)

class Payment(models.Model):
    TYPE_PAYMENT = [
    ('online', 'online'),
    ('offline', 'offline')]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payment')
    status_payment = models.BooleanField(default=False, blank=True)
    type_payment = models.CharField(max_length=10, choices = TYPE_PAYMENT, blank=True)

class OrderDetail(models.Model):
    product_child = models.ForeignKey(ProductChilds, on_delete=models.CASCADE, related_name='order_detail')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_detail')
    quantity = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=0, blank=True)
    total_price = models.FloatField(default=0, blank=True)
    discount = models.FloatField(default=0, blank=True)