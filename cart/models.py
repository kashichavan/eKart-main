from django.db import models
from store.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=250)
    date_created=models.DateTimeField(auto_now=True)

class Cart_items(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)
    

