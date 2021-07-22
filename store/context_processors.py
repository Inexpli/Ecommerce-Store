from .models import Category, Customer, Order


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def basket(request):
    try:
        customer = request.user.customer
    except:
        device = request.META['REMOTE_ADDR']

        customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    return {
        'order': order,
    }
