from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import (BillingForm, ProfileUpdateForm, UserRegisterForm,
                    UserUpdateForm)
from .models import *
from .models import Profile


# Create your views here.
@login_required
def AppointmentView(request):
    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        Appointment.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email,
                                   phone=phone, subject=subject, description=description)

        messages.success(request, f'Appointment booked successfully')

        return redirect('home')

    else:
        Appointment()
        messages.info(request, f'Enter details to create an Appointment')

    return render(request, 'web/make_appointment.html')


def register(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Account Created for {username} please login to continue')
            return redirect('login')

    else:

        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'profile details updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {

        'u_form': u_form,

        'p_form': p_form

    }
    return render(request, 'users/profile.html', context)


def example(request):
    return render(request, 'users/example.html')


@login_required
def Billing(request):
    bill = Billinginfo.objects.filter(user=request.user).first()

    B_form = BillingForm(instance=bill)

    if request.method == 'POST':

        B_form = BillingForm(request.POST, instance=bill)
        if B_form.is_valid():
            bud = B_form.save(commit=False)  # interrupts the save method of the model to set the user, since that was
            # not passed in the model form
            bud.user = request.user
            bud.save()
            messages.success(request, f'Billing Information Saved successfully ')
            return redirect('checkout')


    else:

        B_form = BillingForm(instance=bill)

    return render(request, 'users/billing.html', {'B_form': B_form})


def login2(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, f'{username} is logged in succesfully')
            return redirect('home')
        else:
            messages.error(request, f'invalid credentials')
            return redirect('login2')

    return render(request, 'users/login2.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, f'you have logged out succesfully')
        return redirect('login2')
