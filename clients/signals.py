from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_client_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(user=instance,
                                         fullname=user.username,
                                         email=user.email)


