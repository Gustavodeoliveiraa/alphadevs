from django.db import models
from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=255, blank=False, null=False)
    product_image = models.ImageField(
        upload_to='product_image', blank=False, null=False
    )
    product_description = models.TextField(blank=False, null=False)
    product_category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name='pd_category'
    )
    product_release_date = models.DateField(auto_now_add=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_height = models.DecimalField(max_digits=6, decimal_places=2)
    product_width = models.DecimalField(max_digits=6, decimal_places=2)
