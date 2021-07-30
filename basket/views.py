from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from basket.basket import Basket
from store.models import Product

from .basket import Basket


def basket(request):
    basket = Basket(request)
    return render(request, 'store/basket.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        quantity = int(request.POST.get('quantity'))
        size = int(request.POST.get('size'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=quantity, size=size)
        basket_quantity = basket.__len__()
        response = JsonResponse({'quantity': basket_quantity})
        return response
