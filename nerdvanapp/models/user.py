from django.db import models
from django.contrib.auth.models import AbstractUser
from nerdvanapp.managers import CustomUserManager


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    validated_on = models.DateTimeField(auto_now_add=True)
    email_validated = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'nerdvanapp'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
