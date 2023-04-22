from django.db import models
import uuid

# Create your models here.


class Blogs(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to='images/blogs/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

