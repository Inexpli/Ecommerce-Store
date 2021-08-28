from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from account.models import UserBase
from store.models import Product

from .basket import Basket
from .models import Basket as BasketModel


def basket(request):
    if request.user.is_authenticated:
        user = request.user.id
        total_quantity = BasketModel.objects.filter(user=user).aggregate(
            basket_quantity=Sum('quantity'))['basket_quantity']
        total_price = 0
        for basketitem in BasketModel.objects.filter(user=user):
            total_price += basketitem.item.price * basketitem.quantity
        context = BasketModel.objects.filter(user=user)
        if context:
            error = None
        else:
            error = 'Your basket is empty'
    else:
        context = None
        error = None
        total_price = None
        total_quantity = None
    return render(request, 'basket/basket.html', {'basketmodel': context, 'error': error, 'total_price': total_price, 'total_quantity': total_quantity})


def basket_add(request):
    '''
    Handles data captured from ajax and adds product to basket,
    updates the actual amount of products in basket.
    '''
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


def basket_delete(request):
    '''
    Handles request to delete product from basket
    '''
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response


def basket_update(request):
    '''
    Handles request to update product quantity or size from basket
    '''
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        quantity = int(request.POST.get('quantity'))
        size = int(request.POST.get('size'))
        basket.update(product=product_id, quantity=quantity, size=size)

        response = JsonResponse({'Success': True})
        return response


@login_required
def auth_basket_add(request):
    user = get_object_or_404(UserBase, id=request.user.id)
    if request.POST.get('action') == 'post':
        itemID = int(request.POST.get('itemid'))
        quantity = int(request.POST.get('quantity'))
        size = int(request.POST.get('size'))
        product = get_object_or_404(Product, id=itemID)
        if BasketModel.objects.filter(user=user, item=product).exists():
            pass
        else:
            BasketModel.objects.create(
                user=user, item=product, quantity=quantity, size=size)

        response = JsonResponse({'success': 'Added'})
        return response


@login_required
def auth_basket_remove(request):
    user = get_object_or_404(UserBase, id=request.user.id)
    if request.POST.get('action') == 'post':
        itemID = int(request.POST.get('itemid'))
        product = get_object_or_404(Product, id=itemID)
        BasketModel.objects.filter(user=user, item=product).delete()

        response = JsonResponse({'success': 'Removed'})
        return response


@login_required
def auth_basket_update(request):
    user = get_object_or_404(UserBase, id=request.user.id)
    if request.POST.get('action') == 'post':
        itemID = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=itemID)
        quantity = int(request.POST.get('quantity'))
        size = int(request.POST.get('size'))
        BasketModel.objects.filter(user=user, item=product).update(
            quantity=quantity, size=size)

        response = JsonResponse({'success': 'Removed'})
        return response
