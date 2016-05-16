from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name
