from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import stripe
from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '0')
    total = int(total)
    print(total)

    stripe.api_key = 'sk_test_51JO7QyCuKlRfgeZfSkFevG8vmnVIn6OcXC6PdECdxpqipG3TtDh5Tb66se2B7SdwNl5cEi2A3ZacagJHmWWTHi8A008qZjPcpu'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/payment.html', {'client_secret': intent.client_secret})
