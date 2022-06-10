"""it_next URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from unicodedata import name
from django import urls
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from web import views as myview
from users import views as userview
from django.contrib.auth import views as auth_view

from rest_framework import routers
from users import api_views

# define a rounter and register the restframework views
router = routers.DefaultRouter()
router.register('billinginfo', api_views.BillinginfoViewSet)
router.register('user', api_views.UserViewSet)

urlpatterns = [

    path("__debug__/", include('debug_toolbar.urls')),
    # This has been added to support the restframework
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

    # This has been added to support the allauth library
    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),
    path('home/', include('web.urls')),

    path('', myview.home, name='home'),
    path('billing-page/', userview.Billing, name='billing_page'),

    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logoutpage/", userview.logoutpage, name="logoutpage"),
    # path('login2/', auth_view.LoginView.as_view(template_name= 'users/login2.html'), name = 'login2'),

    path('login2/', userview.login2, name="login2"),

    path('register/', userview.register, name='register'),
    path('profile/', userview.profile, name='profile'),
    path('example/', userview.example, name='example'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('test/', myview.test, name='test')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
