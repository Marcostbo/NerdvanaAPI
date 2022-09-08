from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=60, unique=True)
    search_name = models.CharField(max_length=60, unique=True)
    link = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
