from django.contrib import admin

from .models import Movie, Genre

# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['__str__', 'fsk']
    list_filter = ['genres', 'fsk']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'count_movies']