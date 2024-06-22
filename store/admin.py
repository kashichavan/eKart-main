from django.contrib import admin
from django.contrib.admin import register
# Register your models here.
from .models import Product

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('product_name',)
    }
    list_display=['product_name','price','images','stock']


