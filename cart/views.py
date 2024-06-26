from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
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

    return redirect('/cart/')
    return redirect('/store/')


def cart(request,total=0,quantity=0,cart_item=None):
    grandtotal=0
    tax=0
    try:
        cart=Cart.objects.get(cart_id=get_cart_id(request))
        cart_items=Cart_items.objects.filter(is_active=True,cart=cart)
        
        for item in cart_items:
            total+=item.product.price*item.quantity
            quantity+=item.quantity
        tax=(2*total)/100
        grandtotal+=total+tax

    except Exception :
        pass

    cart_data={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'total':total,
        'grandtotal':grandtotal,
        'tax':tax,
    }

    return render(request,'cart.html',cart_data)
    
def remove_item(request,product_id):
    cart=Cart.objects.get(cart_id=get_cart_id(request))
    product=get_object_or_404(Product,id=product_id)

    item=Cart_items.objects.get(cart=cart,product=product)

    if item.quantity>1:
        item.quantity-=1
        item.save()
    else:
        item.delete()
    


    return redirect('/cart/')

def remove_one(request,product_id):
    cart=Cart.objects.get(cart_id=get_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    item=Cart_items.objects.filter(cart=cart,product=product_id)

    item.delete()

    return redirect('/cart/')
    
    
