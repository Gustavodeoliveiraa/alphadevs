from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cart.models import Cart


@receiver(post_save, sender=User)
def create_my_cart(sender, instance, *args, **kwargs):
    Cart.objects.create(user=instance)
