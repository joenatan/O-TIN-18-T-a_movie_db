from django.contrib import admin

from .models import Movie, Genre

# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['__str__', 'fsk', 'get_genres']
    list_filter = ['genres', 'fsk']

    def get_genres(self, obj):
        return obj.genres_printable_list
    get_genres.short_description = 'Genres'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'count_movies']