from django.contrib import admin
from .models import Task, BlogPost, Tags

# Register your models here.

admin.site.register(Task)
admin.site.register(Tags)
admin.site.register(BlogPost)