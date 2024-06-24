from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse 
from store.models import Product
from .models import Cart,Cart_items
# Create your views here.
def get_cart_id(request):
    cart_id=request.session.session_key
    if not cart_id:
        cart_id=request.session.create()
    return cart_id

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=get_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=get_cart_id(request),
        )

    try:
        cart_item=Cart_items.objects.get(cart=cart,product=product)
        cart_item.quantity+=1
        cart_item.save()
    except Cart_items.DoesNotExist:
        cart_item=Cart_items.objects.create(
            product=product,
            cart=cart,
            quantity=1,   
        )
        cart_item.save()

    return redirect('/store/')
    return redirect('/store/')


def cart(request,total=0,quantity=0,cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=get_cart_id(request))
        cart_items=Cart_items.objects.filter(is_active=True,cart=cart)
        for item in cart_items:
            total+=item.product.price*cart_item.quantity
            quantity+=item.quantity
    except Exception :
        pass

    cart_data={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
    }

    return render(request,'cart.html',cart_data)
    


        


    return render(request,'cart.html')
    
    
