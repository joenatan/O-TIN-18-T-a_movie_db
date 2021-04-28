from django.db import models

# https://docs.djangoproject.com/en/3.2/topics/db/models/


class Movie(models.Model):
    # sql -> varchar(256)
    title = models.CharField(max_length=256)
    # sql -> text null
    description = models.TextField(blank=True)
    release_date = models.DateField()
    fsk = models.IntegerField(default=12)
    duration = models.IntegerField(default=0)

    genres = models.ManyToManyField('Genre', related_name='movies')


class Genre(models.Model):
    name = models.CharField(max_length=256)