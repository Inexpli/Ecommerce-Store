from django.contrib import messages
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render

from store.forms import UserRegisterForm

from .models import *

# from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'store/home.html')


def all(request):
    products = Product.products.all()
    context = {
        'products': products,
    }
    return render(request, 'store/all.html', context)


def category(request, slug):
    category_show = get_object_or_404(Category, slug=slug)
    products = Product.products.filter(category_id=category_show)
    context = {
        'category_show': category_show,
        'products': products,
    }
    return render(request, 'store/category.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} has been created!')
            return redirect('/login')
    else:
        form = UserRegisterForm()

    return render(request, 'store/register.html', {'form': form})


def item(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }
    return render(request, 'store/item.html', context)
