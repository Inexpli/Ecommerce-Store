from store.models import Product
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from account.models import UserBase
from .models import List


@login_required
def wishlist_add(request):
    '''
    Adds specific product to user's wishlist
    '''
    user = get_object_or_404(UserBase, id=request.user.id)
    if request.POST.get('action') == 'post':
        itemID = int(request.POST.get('itemid'))
        product = get_object_or_404(Product, id=itemID)
        if List.objects.filter(user=user, item=product).exists():
            pass
        else:
            List.objects.create(user=user, item=product)

        response = JsonResponse({'success': 'Added'})
        return response


@login_required
def wishlist_remove(request):
    '''
    Removes specific product from user's wishlist
    '''
    user = get_object_or_404(UserBase, id=request.user.id)
    if request.POST.get('action') == 'post':
        itemID = int(request.POST.get('itemid'))
        product = get_object_or_404(Product, id=itemID)
        List.objects.filter(user=user, item=product).delete()

        response = JsonResponse({'success': 'Removed'})
        return response


@login_required
def wishlist(request):
    user = request.user.id
    lista = List.objects.filter(user=user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': lista})
