from . import views as myviews
from users.views import AppointmentView
from django.urls import path, include
from . import cart as mycart
from . import checkout
from .decorators import bill_check

urlpatterns = [

    path('', myviews.home, name='home'),
    path('make_appointment/', AppointmentView, name='appointment'),
    path('about/', myviews.about, name='about'),
    path('services/', myviews.services, name='services'),
    path('services_detail/', myviews.services_detail, name='services_detail'),
    path('services_list/', myviews.services_list, name='services_list'),
    path('blog_list/', myviews.blog_list, name='blog_list'),
    path('blog_detail/', myviews.blog_detail, name='blog_detail'),
    path('blog_grid/', myviews.blog_grid, name='blog_grid'),

    path('contact/', myviews.contact, name='contact'),
    path('contact2/', myviews.contact2, name='contact2'),

    path('cart/', myviews.cart, name='cart'),
    path('checkout/', myviews.checkout, name='checkout'),

    path('addtocart/', mycart.addtocart, name='addtocart'),
    path('update-cart/', mycart.updatecart, name='updatecart'),
    path('delete-cart/', mycart.deletecart, name='delete-cart'),

    path('wishlist/', myviews.wishlist, name="wishlist"),
    path('addtowish/', mycart.addtowish, name='addtowish'),
    path('delete-wish/', mycart.deletewish, name="deletewish"),

    path('create-order/', checkout.create_order, name='create-order'),

    path('career/', myviews.career, name='career'),

    path('test/', bill_check(myviews.test), name='test'),
    path('price/', myviews.price, name='price'),

    path('faq/', myviews.faq, name='faq'),
    path('shop/', myviews.shop, name='shop'),
    path('shop_detail/', myviews.shop_detail, name='shop_detail'),
    path('shop_detail2/<str:slug>', myviews.shop_detail2, name='shop_detail2'),

    path('error/', myviews.error, name='error'),
    path('privacy_policy/', myviews.privacy_policy, name='privacy_policy'),
    path('test/', myviews.test, name='test'),

]
