from django.db import models

from researcher.models import Researcher


class Study(models.Model):
    title = models.TextField(default='my study', max_length=100)
    researchers = models.ManyToManyField(Researcher)
    ethics = models.TextField(max_length=4096)