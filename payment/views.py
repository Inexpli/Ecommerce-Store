import json

import stripe

from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required

from basket.basket import Basket
from basket.models import Basket as BasketModel
from orders.views import payment_confirmation


@login_required
def BasketView(request):
    total_price = 0
    for basketitem in BasketModel.objects.filter(user=request.user.id):
        total_price += basketitem.item.price * basketitem.quantity
    total = str(total_price)
    total = total.replace('.', '0')
    total = int(total)

    stripe.api_key = 'sk_test_51JO7QyCuKlRfgeZfSkFevG8vmnVIn6OcXC6PdECdxpqipG3TtDh5Tb66se2B7SdwNl5cEi2A3ZacagJHmWWTHi8A008qZjPcpu'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='usd',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/payment.html', {'client_secret': intent.client_secret})


class Error(TemplateView):
    template_name = 'payment/error.html'


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
