import os
from django.db.models.signals import pre_save, post_delete
from product.models import ProductImage
from django.dispatch import receiver


def delete_image(instance):
    try:
        os.remove(instance.images.path)
    except (ValueError, FileNotFoundError):
        ...


@receiver(pre_save, sender=ProductImage)
def product_image_update(sender, instance, *args, **kwargs):
    try:
        old_instance = ProductImage.objects.get(pk=instance.pk)
        is_new = os.path.basename(old_instance.images.name) != instance.images

        if is_new:
            delete_image(old_instance)
            print(f'deletado {old_instance.images}\n nova imagem {instance.images}')

    except Exception:
        ...


@receiver(post_delete, sender=ProductImage)
def product_image_delete(sender, instance, *args, **kwargs):

    delete_image(instance)
    print(f'deletado imagem {instance.images.name}')

