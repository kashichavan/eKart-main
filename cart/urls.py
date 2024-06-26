from django.urls import path
from .views import *

app_name='cart'


urlpatterns = [
    path('',cart,name='cart'),
    path('add_cart/<int:product_id>/',add_cart,name='add_cart'),
    path('remove_cart/<int:product_id>/',remove_item,name='remove_cart'),
    path('remove_item/<int:product_id>/',remove_one,name='remove_item'),
]
