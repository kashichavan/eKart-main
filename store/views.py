from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def index(request):
    allprodducts=Product.objects.filter(is_avaiable=True)

    data={
        'allproducts':allprodducts
    }
    return render(request,'index.html',data)


def  store(request,category_slug=None):
    categories=None
    allproducts=None
    if category_slug!=None:
        categories=get_object_or_404(Category,slug=category_slug)
        allproducts=Product.objects.filter(category=categories,is_avaiable=True)
        product_count=allproducts.count()
    else:
        allproducts=Product.objects.filter( is_avaiable=True)
        product_count=allproducts.count()
    data={'data':allproducts,'product_count':product_count}
    return render(request,'store.html',data)

def product_details(request,category_slug,product_slug):
    product_=None
    try:
        product_=Product.objects.get(category__slug=category_slug,slug=product_slug)
        
    except Exception as e:
        print(e)
    
    return render(request,'product-detail.html',{'product':product_})

