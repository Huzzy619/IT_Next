from django.contrib import admin
from .models import *
from django.contrib.auth.models import User



@admin.register(Billinginfo)
class BillinginfoAdmin(admin.ModelAdmin):
    list_display= ['user','country', 'postcode', 'phone', 'id_list']
    list_editable= ['country', 'phone']
    list_filter= ['country', 'phone']

    @admin.display(ordering='id')
    def id_list(self,billinginfo):
        return billinginfo.id + 2
    


admin.site.register(Profile)

admin.site.register(Appointment)