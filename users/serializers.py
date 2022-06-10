from .models import Billinginfo
from django.contrib.auth.models import User
from rest_framework import serializers


class BillinginfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billinginfo
        fields =   ['user', 'address', 'email', 'country', 'city', 'postcode', 'phone', 'first_name', 'last_name', 'company_name']  

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password']

