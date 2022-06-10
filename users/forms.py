from django_countries.widgets import CountrySelectWidget 
from django.contrib.auth.models import User 
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from matplotlib import widgets 
from .models import Billinginfo, Profile




class UserRegisterForm(UserCreationForm):

	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	Address = forms.CharField(required =False)

	 

	class Meta:
		model = User
		fields = ['first_name','last_name','username','Address','email','password1','password2']
	
class UserUpdateForm (forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['image']


		
class BillingForm(forms.ModelForm):

	class Meta:
		model = Billinginfo
		fields = ['first_name','last_name','country','city','state', 'postcode', 'phone','address','email']
		widgets = {'country': CountrySelectWidget()}
	 	



