from wishlist.wishlist import WishList
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


def wishlist(request):
    if request.user.is_authenticated:
        user = request.user.id
        context = List.objects.filter(user=user)
        if context:
            error = None
        else:
            error = 'Your wishlist is empty'
    else:
        context = WishList(request)
        error = None
    return render(request, 'wishlist/wishlist.html', {'wishlist': context, 'error': error})


def not_auth_wishlist_add(request):
    wishlist = WishList(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('itemid'))
        product = get_object_or_404(Product, id=product_id)
        wishlist.add(product=product)
        response = JsonResponse({'success': 'Added'})
        return response


def not_auth_wishlist_delete(request):
    wishlist = WishList(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('itemid'))
        wishlist.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response
