from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def BasketView(request):
    return render(request, 'payment/payment.html')
