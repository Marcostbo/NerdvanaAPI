from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=60, unique=True)
    release = models.DateField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    storyline = models.TextField(blank=True, null=True)
    console = models.ManyToManyField('Console')
    game_company = models.ForeignKey('GameCompany', on_delete=models.CASCADE, blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        indexes = [
            models.Index(fields=['name']),
        ]
