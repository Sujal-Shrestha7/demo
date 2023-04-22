from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=True, blank=True)
    short_intro = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(default='images/experts/profile_photo/user-default.png',
                                        upload_to='images/clients/profile_photo', null=True, blank=True)

    def __str__(self):
        return self.full_name


