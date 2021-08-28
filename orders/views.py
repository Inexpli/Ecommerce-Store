from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from basket.basket import Basket
from basket.models import Basket as BasketModel
from store.models import Product

from .models import Order

now = datetime.now()


@login_required
def add(request):
    '''
    Creates order if payment has been completed
    '''
    if request.POST.get('action') == 'post':
        order_key = request.POST.get('order_key')
        user_id = request.user.id
        total_price = 0
        for basketitem in BasketModel.objects.filter(user=user_id):
            total_price += basketitem.item.price * basketitem.quantity
        baskettotal = total_price
        full_name = request.POST.get('custName')
        town = request.POST.get('custTown')
        address1 = request.POST.get('custAdd')
        address2 = request.POST.get('custAdd2')
        postcode = request.POST.get('custCode')
        country = request.POST.get('custCountry')

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            for basketitem in BasketModel.objects.filter(user=user_id):
                product = get_object_or_404(Product, id=basketitem.item.id)
                order = Order.objects.create(user_id=user_id, product=product, size=basketitem.size, quantity=basketitem.quantity, full_name=full_name, address1=address1,
                                             address2=address2, postcode=postcode, town=town, country=country, total_paid=baskettotal, order_key=order_key, authenticated=True)

        response = JsonResponse({'success': 'Return authenticated orders'})
        return response


def payment_confirmation(data):
    '''
    Updates billing status to True if order_key captured by stripe exists
    '''
    Order.objects.filter(order_key=data).update(billing_status=True)


@login_required
def dashboard(request):
    user = request.user.id
    order = Order.objects.filter(user=user, billing_status=True)
    return render(request, 'orders/dashboard.html', {'orders': order})


@login_required
def order_done(request):
    BasketModel.objects.filter(user=request.user.id).delete()
    return render(request, 'orders/order_done.html')
