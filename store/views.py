from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def home(request):
    return render(request, 'store/home.html')

def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'store/products.html', context)

def item(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {
        'product': product,
    }
    return render(request, 'store/item.html', context)
