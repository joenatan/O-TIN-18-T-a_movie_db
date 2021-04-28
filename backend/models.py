from django.db import models

# https://docs.djangoproject.com/en/3.2/topics/db/models/

# bei jeder änderung (model Attribute) muss makemigrations und migrate durchgeführt werden


class Movie(models.Model):
    # sql -> varchar(256)
    title = models.CharField(max_length=256)
    # sql -> text null
    description = models.TextField(blank=True)
    release_date = models.DateField()
    fsk = models.IntegerField(default=12)
    duration = models.IntegerField(default=0)

    genres = models.ManyToManyField('Genre', related_name='movies')


    def __str__(self):
        return self.title
        


class Genre(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    @property
    def count_movies(self):
        """
        Return count movies of current instance
        """
        return self.movies.select_related().count()