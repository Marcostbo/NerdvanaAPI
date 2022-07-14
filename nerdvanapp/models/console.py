from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=20, unique=True)
    initials = models.CharField(max_length=20, unique=True)
    release = models.DateField()
    description = models.TextField()
    family = models.ForeignKey('Family', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    twitch_id = models.IntegerField(default=None, null=True, verbose_name='Twitch ID')

    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Family'
        verbose_name_plural = 'Families'


class Company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    foundation = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
