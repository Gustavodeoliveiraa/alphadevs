from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name', 'product_image', 'product_description',
        'product_category', 'product_release_date', 'product_price',
        'product_height', 'product_width'
    ]
    search_fields = ['product_name']
