from django.urls import path
from .views import store,product_details,search,home


app_name='store'

urlpatterns = [
    path('',store,name='store'),
    path('<slug:category_slug>/',store,name='store'),
    path('<slug:category_slug>/<slug:product_slug>',product_details,name='product_details'),
    path('search/',search,name='search'),
    path('home/',home,name='home')
]

