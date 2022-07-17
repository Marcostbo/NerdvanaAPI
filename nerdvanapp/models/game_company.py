from django.db import models


class GameCompany(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
