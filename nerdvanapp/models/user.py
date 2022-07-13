from django.db import models
from django.contrib.auth.models import AbstractUser
from nerdvanapp.managers import CustomUserManager


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'nerdvanapp'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
