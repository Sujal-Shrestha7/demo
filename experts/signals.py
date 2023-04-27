from django.db.models.signals import post_save, post_delete
from .models import Experts
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_expert_profile(sender, instance, created, **kwargs):
    if created:
        expert = Experts.objects.create(user=instance,
                                        username=instance.username,
                                        email=instance.email)
        subject = 'Welcome to Expertise Hub !!!'
        message = 'We are glad to have you here. Click here to submit your cv. https://meta.facebook.register-form'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [expert.email],
            fail_silently=False
        )


@receiver(post_save, sender=Experts)
def update_expert_profile(sender, instance, created, **kwargs):
    expert = instance
    user = expert.user
    if not created:
        user.username = expert.full_name
        user.save()


@receiver(post_delete, sender=Experts)
def delete_expert(sender, instance, **kwargs):
    user = instance.user
    user.delete()
