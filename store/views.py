from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from store.forms import UserRegisterForm

from .models import Category, Customer, Order, OrderItem, Product

# from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'store/home.html')


def all(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store/all.html', context)


def category(request, slug):
    category_show = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category_id=category_show)
    context = {
        'category_show': category_show,
        'products': products,
    }
    return render(request, 'store/category.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'store/register.html', {'form': form})


def item(request, slug, pk):
    product = get_object_or_404(Product, slug=slug)
    productID = Product.objects.get(id=pk)

    if request.method == 'POST':
        productID = Product.objects.get(id=pk)
        # Get user account information
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(
            order=order, product=productID)
        orderItem.quantity = request.POST['quantity']
        orderItem.save()

        redirect('store:basket')  # TO FIX

    context = {
        'product': product,
    }
    return render(request, 'store/item.html', context)


# def product(request, pk):
# 	product = Product.objects.get(id=pk)

# 	if request.method == 'POST':
# 		product = Product.objects.get(id=pk)
# 		#Get user account information
# 		try:
# 			customer = request.user.customer
# 		except:
# 			device = request.COOKIES['device']
# 			customer, created = Customer.objects.get_or_create(device=device)

# 		order, created = Order.objects.get_or_create(customer=customer, complete=False)
# 		orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
# 		orderItem.quantity=request.POST['quantity']
# 		orderItem.save()

# 		return redirect('store:basket')

# 	context = {'product':product}
# 	return render(request, 'store/product.html', context)


def basket(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    context = {'order': order}
    return render(request, 'store/basket.html', context)
