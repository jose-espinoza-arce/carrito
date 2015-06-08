import os
import uuid

from django.dispatch import receiver

from django.conf import settings

from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractProductClass


class Product(AbstractProduct):
    event_type = models.TextField(max_length=255, default='Fiesta')
    #categories = models.TextField(max_length=255, blank=True)
    bottlesize = models.CharField(max_length=20, blank=True)
    bottles = models.PositiveSmallIntegerField(blank=True)
    maxlabels = models.PositiveSmallIntegerField(blank=True)
    bottlerow = models.PositiveSmallIntegerField(blank=True)
    img_original_size = models.ImageField(
        upload_to='images/catalogue/product/',
        default=os.path.join(settings.MEDIA_ROOT, 'generic_profile_image.png'),
    )
    img_zoom_size = models.ImageField(
        upload_to='images/catalogue/product',
        default=os.path.join(settings.MEDIA_ROOT, 'generic_profile_image.png'),
    )
    img_tag = models.ImageField(
        upload_to='images/catalogue/product',
        default=os.path.join(settings.MEDIA_ROOT, 'generic_profile_image.png'),
    )
    #type = models.ForeignKey('TequilaType', default=1, related_name='sizes')

    def __unicode__(self):
        return self.bottlesize


class ProductClass(AbstractProductClass):
    bimage = models.ImageField(
        verbose_name='Imagen',
        upload_to='images/catalogo/',
        default=os.path.join('images', 'catalogo', 'generic_profile_image.png'),
        )
    tag_img = models.ImageField(
        verbose_name='Imagen',
        upload_to='images/catalogo/',
        default=os.path.join('images', 'catalogo', 'generic_profile_image.png'),
        )

# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=ProductClass)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.bimage:
        if os.path.isfile(instance.bimage.path):
            os.remove(instance.bimage.path)

    if instance.tag_img:
        if os.path.isfile(instance.tag_img.path):
            os.remove(instance.tag_img.path)

@receiver(models.signals.pre_save, sender=ProductClass)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if not instance.pk:
        return False

    try:
        old_file = ProductClass.objects.get(pk=instance.pk).bimage
    except ProductClass.DoesNotExist:
        return False

    new_file = instance.bimage
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    try:
        old_file = ProductClass.objects.get(pk=instance.pk).tag_img
    except ProductClass.DoesNotExist:
        return False

    new_file = instance.tag_img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.img_original_size:
        if os.path.isfile(instance.img_original_size.path):
            os.remove(instance.img_original_size.path)

    if instance.img_zoom_size:
        if os.path.isfile(instance.img_original_size.path):
            os.remove(instance.img_original_size.path)

    if instance.img_tag:
        if os.path.isfile(instance.img_original_size.path):
            os.remove(instance.img_original_size.path)

@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if not instance.pk:
        return False
    #images = [img_original_size, ]
    try:
        old_file = Product.objects.get(pk=instance.pk).img_original_size
    except Product.DoesNotExist:
        return False

    new_file = instance.img_original_size
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    try:
        old_file = Product.objects.get(pk=instance.pk).img_zoom_size
    except ProductClass.DoesNotExist:
        return False

    new_file = instance.img_zoom_size
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    try:
        old_file = Product.objects.get(pk=instance.pk).img_tag
    except ProductClass.DoesNotExist:
        return False

    new_file = instance.img_tag
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)




from oscar.apps.catalogue.models import *