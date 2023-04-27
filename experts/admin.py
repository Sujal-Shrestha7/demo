from django.contrib import admin
from .models import Experts, Educations, Experiences, Skills, Categories, Message

# Register your models here.

admin.site.register(Experts)
admin.site.register(Educations)
admin.site.register(Experiences)
admin.site.register(Skills)
admin.site.register(Categories)
admin.site.register(Message)