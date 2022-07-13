from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=20, unique=True)
    initials = models.CharField(max_length=20, unique=True)
    release = models.DateField()
    description = models.TextField()
    family = models.ForeignKey('Family', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    foundation = models.DateField()

    def __str__(self):
        return self.name
