from django.db import models
from django.conf import settings
import uuid
from experts.models import Categories

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    preferred_expertise = models.ManyToManyField(Categories)
    short_intro = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(default='images/experts/profile_photo/user-default.png',
                                        upload_to='images/clients/profile_photo', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.username


