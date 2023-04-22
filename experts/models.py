import uuid
from django.db import models
from django.conf import settings

# Create your models here.


class Experts(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    profile_photo = models.ImageField(default='images/experts/profile_photo/user-default.png',
                                      upload_to='images/experts/profile_photo', null=True, blank=True)
    short_intro = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    categories = models.ForeignKey('Categories', related_name='categories', on_delete=models.CASCADE,
                                   null=True, blank=True)
    github_link = models.URLField(max_length=1000, null=True, blank=True)
    linkedin_link = models.URLField(max_length=1000, null=True, blank=True)
    website_link = models.URLField(max_length=1000, null=True, blank=True)
    twitter_link = models.URLField(max_length=1000, null=True, blank=True)
    youtube_link = models.URLField(max_length=1000, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Categories(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100)
    categories_image = models.ImageField(default='images/default.jpg', upload_to='images/categories', null=True,
                                         blank=True)

    def __str__(self):
        return self.title


class Educations(models.Model):
    DEGREE_OPTIONS = (
        ('Doctorate', 'Doctorate'),
        ('Master', 'Master'),
        ('Bachelor', 'Bachelor'),
        ('Intermediate', 'Intermediate')
    )
    experts = models.ForeignKey('Experts', related_name='educations', on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    degree = models.CharField(max_length=100, default='None', choices=DEGREE_OPTIONS, null=True, blank=True)
    title = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100, null=True, blank=True)
    institute_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Experiences(models.Model):
    POSITION_CHOICES = (
        ('Senior', 'Sr.'),
        ('Mid Level', 'Mid.'),
        ('Junior', 'Jr.'),
        ('Intern', 'Intern')
    )
    experts = models.ForeignKey('Experts', related_name='experiences', on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default='Trainee', choices=POSITION_CHOICES,
                                null=True, blank=True)
    duration = models.PositiveSmallIntegerField(default='1')
    is_working = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Skills(models.Model):
    experts = models.ForeignKey('Experts', related_name='skills', on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

