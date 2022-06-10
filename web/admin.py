import imp
from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from .models import *


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'quantity', 'old_price', 'new_price', 'quantity_status']
    list_editable = ['quantity', 'old_price', 'new_price']

    @admin.display(ordering='quantity')
    def quantity_status(self, product):
        if product.quantity < 1:
            return "Out Stock"
        return "In Stock"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'tracking_id', 'status', 'order_count']
    list_editable = ['status']

    @admin.display(ordering='order_count')
    def order_count(self, order):
        # reverse('admin:')

        return format_html("<a href="">{}</a>", order.order_count)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_count=Count('orderitems')
        )
@admin.register(OrderItems)
class OrderItemsAdnin(admin.ModelAdmin):
    list_display= ['name', 'price', 'qty', 'id_order_info']

    @admin.display(ordering='order')
    def id_order_info (self, orderitems):
        url = reverse('admin:web_order_changelist') + '?' + urlencode({'order__id': str(orderitems.order.id)})
        return format_html("<a href='{}'>{}</a>",url, orderitems.order.tracking_id)
        

admin.site.register(Comment)
# admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Contact)
admin.site.register(Wishlist)

