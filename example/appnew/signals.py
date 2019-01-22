from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Item, Storage, ClassesChar, Character


@receiver(post_save, sender=Item)
def create_item_storage(sender, instance, created, **kwargs):
    print(created)
    print(instance)
    if created:
        Storage.objects.create(item=instance, quantity=5)


@receiver(post_save, sender=Character)
def create_classes_clas(sender, instance, created, **kwargs):
    if created:
        ClassesChar.objects.create(char=instance, choice=2)

