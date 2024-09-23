import os
from django.conf import settings
from django.db import models
from category.models import Category
from PIL import Image


class Product(models.Model):
    product_name = models.CharField(max_length=255, blank=False, null=False)
    product_description = models.TextField(blank=False, null=False)
    product_category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name='pd_category'
    )
    product_release_date = models.DateField(auto_now_add=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_height = models.DecimalField(max_digits=6, decimal_places=2)
    product_width = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='images'
    )

    images = models.ImageField(
        upload_to='product_image', blank=False, null=False
    )

    @staticmethod
    def resize_image(image, width=1330):
        image_full_path = image.path
        image_pillow = Image.open(image_full_path)

        original_width, original_hight = image_pillow.size

        if original_width < width:
            image_pillow.close()
            return

        new_hight = round((width * original_hight) / original_width)

        new_image = image_pillow.resize((width, new_hight), Image.LANCZOS)

        new_image.save(
            image_full_path,
            optimize=True,
            quality=100
        )

    def save(self, *args, **kwargs):
        saved = super().save(*args, **kwargs)

        if self.images:
            self.resize_image(self.images)

        return saved
