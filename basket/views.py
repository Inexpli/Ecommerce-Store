from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse

from .basket import Basket
from store.models import Product

def basket_summary(request):
    return render(request, 'basket/summary.html')

def basket_add(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']


        

