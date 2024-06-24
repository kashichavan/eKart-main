from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# Register your models here.

@register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['cart_id']

@register(Cart_items)
class Cart_itemsAdmin(admin.ModelAdmin):
    list_display=['product','cart','quantity']