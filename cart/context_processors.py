from .models import *

def getItems(request):
    cart=Cart_items.objects.all().count()
    return dict(total=cart)



