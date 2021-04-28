from django.contrib import admin

from .models import Movie, Genre, Person, PersonMovie

# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['__str__', 'fsk', 'get_genres', 
        'get_directors', 'get_actors']
    list_filter = ['genres', 'fsk']

    def get_genres(self, obj):
        return obj.genres_printable_list
    get_genres.short_description = 'Genres'

    def get_directors(self, obj):
        return obj.people_printable_list('director')
    get_directors.short_description = 'Directors'

    def get_actors(self, obj):
        return obj.people_printable_list('actor')
    get_actors.short_description = 'Actors'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'count_movies']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(PersonMovie)
class PersonMovieAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'get_movie', 'type']
    list_filter = ['type']

    def get_movie(self, obj):
        return obj.print_movie
