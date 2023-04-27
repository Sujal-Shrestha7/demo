from .models import Client
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_client_profile(sender, instance, created, **kwargs):
    user = instance
    print('Client signals triggered')
    if created:
        client = Client.objects.create(user=instance,
                                       username=user.username,
                                       email=user.email)
    print('Signal TErminated')


@receiver(post_save, sender=Client)
def update_client_profile(sender, instance, created, **kwargs):
    client = instance
    user = client.user
    if not created:
        user.username = client.full_name
        user.save()


@receiver(post_delete, sender=Client)
def delete_expert(sender, instance, **kwargs):
    user = instance.user
    user.delete()
