from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from web.models import Product, Cart, Wishlist


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('prod_id')
            product_check = Product.objects.get(id=prod_id)

            if product_check:
                if Cart.objects.filter(user=request.user.id, product_id=prod_id):
                    return JsonResponse({'status': "Product Already in Cart"})

                else:
                    product_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= product_qty:

                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=product_qty)
                        return JsonResponse({'status': "Product added successfully"})
                    else:
                        return JsonResponse({'status': "Only " + str(product_check.quantity) + " is available"})

            else:
                return JsonResponse({'status': "No such product found"})

        else:

            return JsonResponse({'status': "Login to continue"})
    else:
        return JsonResponse({'status': "Not valid"})


def addtowish(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('prod_id')
            product_check = Product.objects.get(id=prod_id)

            if (product_check):
                if (Wishlist.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Product already in Wishlist"})
                elif (Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Can't add to wishlist because product is already in Cart"})

                else:
                    product_qty = int(request.POST.get('product_qty'))

                    Wishlist.objects.create(user=request.user, product_id=prod_id, product_qty=product_qty)
                    return JsonResponse({'status': "Product added to Wishlist successfully"})




            else:
                return JsonResponse({'status': "No such product found"})


        else:

            return JsonResponse({'status': "Login to continue"})
    else:
        return JsonResponse({'status': "Not valid"})


def updatecart(request):
    if request.method == "POST":
        prod_id = int(request.POST['prod_id'])

        if (Cart.objects.filter(product_id=prod_id, user=request.user)):
            new_product_qty = int(request.POST['product_qty'])

            Cart.objects.filter(product_id=prod_id, user=request.user) \
                .update(product_qty=new_product_qty)

            # cart.product_qty = new_product_qty 

            # cart.save()
            # cart.update(product_qty = new_product_qty)

            return JsonResponse({'status': "Cart updated"})

    return redirect('home')


def deletecart(request):
    if request.method == 'POST':

        prod_id = int(request.POST.get('prod_id'))

        if request.user.is_authenticated:
            # prod_id  = int(request.POST.get('prod_id'))
            # print(prod_id)
            if Cart.objects.filter(user=request.user, product_id=prod_id).exists():

                cart = Cart.objects.get(user=request.user, product_id=prod_id)

                cart.delete()
                return JsonResponse({'status': "cart deleted sucessfully"})

            else:
                return JsonResponse({'status': "No such product in cart"})

        else:
            return JsonResponse({'status': 'You must log in to delete cart'})

    else:
        return redirect('home')


def deletewish(request):
    if request.method == 'POST':

        prod_id = int(request.POST.get('prod_id'))

        if request.user.is_authenticated:
            # prod_id  = int(request.POST.get('prod_id'))
            # print(prod_id)
            if (Wishlist.objects.filter(user=request.user, product_id=prod_id).exists()):

                wish = Wishlist.objects.get(user=request.user, product_id=prod_id)

                wish.delete()
                return JsonResponse({'status': "item removed from wishlist sucessfully"})

            else:
                return JsonResponse({'status': "No such product in wishlist"})

        else:
            return JsonResponse({'status': 'You must log in to delete any item from wishlist'})

    else:
        return redirect('home')
