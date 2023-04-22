from django.db.models.signals import post_save, post_delete
from .models import Experts
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_expert_profile(sender, instance, created, **kwargs):
    if created:
        Experts.objects.create(user=instance,
                               username=instance.username,
                               email=instance.email)


@receiver(post_save, sender=Experts)
def update_expert_profile(sender, instance, created, **kwargs):
    expert = instance
    user = expert.user
    if not created:
        user.username = expert.full_name
        user.save()


# @receiver(post_save, sender=User)
# def update_expert_profile(sender, instance, created, **kwargs):
#
#     user = instance
#     if not created:
#         user.username = expert.full_name
#         user.save()


@receiver(post_delete, sender=Experts)
def delete_expert(sender, instance, **kwargs):
    print('invoked deleted !!!')
    user = instance.user
    user.delete()
