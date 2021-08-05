from django.http import request
from django.shortcuts import get_object_or_404, render

from store.forms import UserRegisterForm

from .models import *


def home(request):
    return render(request, 'store/home.html')


def all(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store/all.html', context)


def category(request, slug):
    category_show = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category_id=category_show)
    context = {
        'category_show': category_show,
        'products': products,
    }
    return render(request, 'store/category.html', context)


def item(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }
    return render(request, 'store/item.html', context)
