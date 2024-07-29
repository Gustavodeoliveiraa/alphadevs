from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, blank=False, null=False
    )


class CartItem(models.Model):
    cart = models.ForeignKey(
        to=Cart, on_delete=models.CASCADE, blank=False, null=False
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, blank=False, null=False
    )
    quantity = models.IntegerField(default=1, blank=False, null=False)