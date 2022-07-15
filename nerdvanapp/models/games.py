from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=20, unique=True)
    release = models.DateField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    storyline = models.TextField(blank=True, null=True)
    console = models.ManyToManyField('Console')
    rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rating_count = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
