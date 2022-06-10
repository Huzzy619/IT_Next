from tabnanny import check
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart, Wishlist

@receiver(post_save, sender = Cart)
def delete_cart (sender, created, instance, **kwargs):
    if created:
        check=  instance.product.id
        if Wishlist.objects.filter(user = instance.user, product_id = check ).exists():
            wish = Wishlist.objects.get(user = instance.user, product_id = check )
            wish.delete()
            
