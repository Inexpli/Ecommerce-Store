from django.http import request
from django.shortcuts import render
from django.http.response import JsonResponse

from basket.basket import Basket
from .models import Order, OrderItem


def add(request):
    '''
    Creates order if payment has been completed
    '''
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()

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
            order = Order.objects.create(user_id=user_id, full_name=full_name, address1=address1,
                                         address2=address2, postcode=postcode, town=town, country=country, total_paid=baskettotal, order_key=order_key)
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(
                    order_id=order_id, product=item['product'], price=item['price'], quantity=item['quantity'])

        response = JsonResponse({'success': 'Return something'})
        return response


def payment_confirmation(data):
    '''
    Updates billing status to True if order_key captured by stripe exists
    '''
    Order.objects.filter(order_key=data).update(billing_status=True)


def dashboard(request):
    basket = Basket(request)
    basket.clear()
    user = request.user.id
    orders = Order.objects.filter(user=user, billing_status=True)

    return render(request, 'orders/dashboard.html', {'orders': orders})


def order_done(request):
    return render(request, 'orders/order_done.html')
