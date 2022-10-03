import random

from django.contrib import messages
from django.http import JsonResponse

from .models import *


def create_order(request):
    neworder = Order()
    if request.method == 'POST':
        neworder.user = request.user
        neworder.first_name = request.POST['firstname']
        neworder.last_name = request.POST['lastname']
        neworder.address = request.POST['address']
        neworder.country = request.POST['country']
        neworder.city = request.POST['city']
        neworder.state = request.POST['state']
        neworder.postcode = request.POST['postcode']
        neworder.email = request.POST['email']
        neworder.phone = request.POST['phone']

        track = random.randint(1111111, 9999999)
        while Order.objects.filter(tracking_id=track):
            track = random.randint(1111111, 9999999)

        neworder.tracking_id = track
        neworder.save()
        cart = Cart.objects.filter(user=request.user)
        product = cart.product_set.all()
        if OrderItems.objects.filter(order=neworder, name=cart.product__product_name, price=cart.product__new_price, qty=cart.product_qty).exists():
            messages.error(request, "Order created already")
            return JsonResponse({'status': 'Order created already'})
        else:

            if cart:
                for item in cart:
                    OrderItems.objects.create(
                        order=neworder, name=item.product.product_name, mprice=item.product.new_price, qty=item.product_qty)

            # cart.delete()
                    messages.success(request, "Order created successfully")
                    return JsonResponse({'status': "Order created successfully"})
            else:
                return JsonResponse({'status': "Order cannot be placed with an empty cart"})

    # return redirect('checkout')
