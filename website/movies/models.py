import time 
import os

from django.db import models
from django.conf import settings


class Actor(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(null=True, blank=True, max_length=30)

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30)
    poster = models.ImageField(upload_to=lambda i, f: "%f.jpg" % time.time(),
                               default='default.jpg')
    synopsis = models.TextField(blank=True) 
    popularity = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre)
    cast = models.ManyToManyField(Actor, blank=True)

    def __unicode__(self):
        return self.title
