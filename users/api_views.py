from .models import Billinginfo
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import BillinginfoSerializer, UserSerializer


class BillinginfoViewSet (viewsets.ModelViewSet):
    queryset = Billinginfo.objects.all()
    serializer_class= BillinginfoSerializer


class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer
