from django.db import models
from django.contrib.auth.models import AbstractUser


def get_image_path(instance, filename):
    return 'pictures/user_{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
