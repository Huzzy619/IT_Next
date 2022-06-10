from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .decorators import bill_check
from users.models import Billinginfo
from .models import *
from random import shuffle


# from users.forms import AppointmentForm

# Create your views here.
@bill_check
def test(request):
    product = Product.objects.all()
    cart = Cart.objects.filter(user = request.user)
    # new = cart.product_set.all()
    print(cart)
    # print(new)
    print(product)
    this = product.cart__set.all()
    print(this)
    return HttpResponse("You are good to go ")


def home(request):
    products = Product.objects.filter(status=1)

    context = {
        'products': products
    }

    return render(request, 'web/it_home.html', context)


@login_required
def shop_detail2(request, slug):
    related = Product.objects.all().exclude(slug=slug)[:3]

    if Product.objects.filter(slug=slug, status=1):
        products = Product.objects.filter(slug=slug)

        context = {
            'products': products,
            'related': related,

        }

        return render(request, 'web/shop_detail2.html', context)

    else:

        messages.warning(request, "no such products on our platform")
        return redirect('shop_detail2')


def about(request):
    return render(request, 'web/it_about.html')


@login_required
@bill_check
def checkout(request):
    bill = Billinginfo.objects.get(user=request.user)

    cart = Cart.objects.filter(user=request.user)
    sub_total = 0
    shipping_fee = 5.0
    if cart:
        for item in cart:
            each_total = item.product_qty * item.product.new_price
            sub_total += each_total

        final_total = sub_total + shipping_fee

        context = {
            'shipping_fee': shipping_fee,
            'final_total': final_total,
            'sub_total': sub_total,
            'bill': bill
        }
    else:
        context = {}
    return render(request, 'web/checkout.html', context)


def services(request):
    return render(request, 'web/services.html')


def price(request):
    return render(request, 'web/price.html')


def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = str(request.POST['message'])

        Contact.objects.create(firstname=firstname, lastname=lastname, email=email, phone=phone, message=message)

        messages.success(request, f"Contact made successfully, we'll get back to you shortly")

        return redirect('home')

    return render(request, 'web/contact.html')


def contact2(request):
    return render(request, 'web/contact2.html')


def privacy_policy(request):
    return render(request, 'web/privacy_policy.html')


def faq(request):
    messages.success(request, f'welcome to the FAQ page')
    return render(request, 'web/faq.html')


def shop(request):
    products = Product.objects.filter(status=1)

    context = {
        'products': products
    }

    return render(request, 'web/shop.html', context)


def shop_detail(request):
    return render(request, 'web/shop_detail.html')


def error(request):
    return render(request, 'web/error.html')


def career(request):
    return render(request, 'web/career.html')


@login_required
def wishlist(request):
    wish = Wishlist.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'wish': wish
    }
    return render(request, 'web/wishlist.html', context)


@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).order_by('-created_at')
    shipping_fee = 5.00
    # print (item_number)

    # calc = Cart.objects.get(user = request.user).
    Sub_total = 0
    if cart:
        for item in cart:
            total = item.product_qty * item.product.new_price

            Sub_total += total

        total_cart_price = Sub_total + shipping_fee

        # print (total_amount)
        context = {
            'cart': list(cart),
            'total_cart_price': total_cart_price,
            'Sub_total': Sub_total,
            'shipping_fee': shipping_fee,

        }
    else:
        context = {}

    return render(request, 'web/cart.html', context)


def services_detail(request):
    return render(request, 'web/services_detail.html')


def services_list(request):
    return render(request, 'web/services_list.html')


def blog_detail(request):
    return render(request, 'web/blog_detail.html')


def blog_list(request):
    return render(request, 'web/blog_list.html')


def blog_grid(request):
    return render(request, 'web/blog_grid.html')


@login_required
def shopping(request, slug):
    if Product.objects.filter(slug=slug, status=1):
        products = Product.objects.filter(slug=slug)

        context = {
            'products': products
        }


    else:
        messages.info(request, f'could not find product')

    return render(request, 'web/shop_detail2.html', context)
