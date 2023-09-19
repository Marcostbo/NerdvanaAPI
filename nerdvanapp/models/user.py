from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from nerdvanapp.managers import CustomUserManager


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    validated_on = models.DateTimeField(null=True)
    email_validated = models.BooleanField(default=False)
    password_changed = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'nerdvanapp'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def validate(self):
        self.validated_on = timezone.now()
        self.email_validated = True
        self.save(update_fields=['validated_on', 'email_validated'])

    def change_password(self, new_password):
        self.password_changed = True
        self.set_password(
            raw_password=new_password
        )
        self.save()
