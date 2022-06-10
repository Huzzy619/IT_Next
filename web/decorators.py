from django.shortcuts import redirect

from users.models import Billinginfo
from django.contrib import messages


def bill_check(view_func):
    def func_wrapper(request, *args, **kwargs):
        if Billinginfo.objects.filter(user=request.user).exists():
            return view_func(request, *args, **kwargs)
        else:
            messages.info(request, f"Kindly fill out your Billing information")
            return redirect('billing_page')

    return func_wrapper
