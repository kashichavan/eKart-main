from .models import Category

def dropdown(request):
    dropdowndata=Category.objects.all()
    return dict(dropdown=dropdowndata)