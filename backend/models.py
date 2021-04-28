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
        
    @property
    def genres_printable_list(self):
        return list(self.genres.select_related())
        
    def people_printable_list(self, person_type):
        # https://docs.djangoproject.com/en/3.2/ref/models/querysets
        people = self.person_movies.select_related().filter(type=person_type)
        return list(people)


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


class Person(models.Model):
    last_name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    age = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return '%s %s (%i)' % (self.first_name, self.last_name, self.age)


# https://docs.djangoproject.com/en/3.2/ref/models/fields/#choices

PERSON_TYPE_CHOICES = (
    ('actor', 'Actor'),
    ('director', 'Director')
)

class PersonMovie(models.Model):
    type = models.CharField(max_length=30, choices=PERSON_TYPE_CHOICES, default='actor')

    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='person_movies')
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='person_movies')

    def __str__(self):
        return '%s %s' % (self.person.first_name, self.person.last_name)

    @property
    def full_name(self):
        return '%s %s' % (self.person.first_name, self.person.last_name)

    @property
    def print_movie(self):
        return self.movie.title