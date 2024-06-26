from .models import Cart_items,Cart
from .views import get_cart_id

def getItems(request):
    count=0
    try:
        cart=Cart.objects.get(cart_id=get_cart_id(request))
        cart_items=Cart_items.objects.all().filter(cart=cart)
        for i in cart_items:
            count+=i.quantity
    except Cart.DoesNotExist:
        count=0
    return dict(cartcount=count)



