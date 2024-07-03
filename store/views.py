from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Product
from category.models import Category
from cart.models import Cart,Cart_items
from cart.views import get_cart_id
from django.core.paginator import Paginator
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
        pagination=Paginator(allproducts,3)
        page=request.GET.get('page')
        page_data=pagination.get_page(page)
        print(page_data.number)
        product_count=allproducts.count()
    else:
        allproducts=Product.objects.filter( is_avaiable=True)
        pagination=Paginator(allproducts,3)
        page=request.GET.get('page')
        page_data=pagination.get_page(page)
        print(page_data.number)
        product_count=allproducts.count()
    data={'data':page_data,'product_count':product_count}
    return render(request,'store.html',data)

def product_details(request,category_slug,product_slug):
    product_=None
    try:
        product_=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        print(e)
    
    return render(request,'product-detail.html',{'product':product_,})
 

def search(request):
    data=request.GET.get('keyword')
    if data!=None:
        res=Product.objects.filter(product_name__icontains=data)
        product_count=res.count()
    else:
        res=Product.objects.filter( is_avaiable=True)
        product_count=res.count()
    data={'data':res,'product_count':product_count}
    return render(request,'store.html',data)


def home(request):
    return HttpResponse("<h1>this is search</h1>")