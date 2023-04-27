from django.db import models
from django.conf import settings
import uuid
from experts.models import Experts
from clients.models import Client

# Create your models here.


class BlogPost(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(default='images/experts/profile_photo/user-default.png',
                                      upload_to='images/posts', null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Tags(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True, related_name='tags')
    title = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Task(models.Model):
    STATUS_OPTION = (
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_post')
    expert = models.ForeignKey(Experts, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='expert_task')
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=False)
    status = models.CharField(choices=STATUS_OPTION, default='New', blank=True, null=True, max_length=100)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
