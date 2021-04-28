from django.contrib import admin

from .models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass    # wird benötigt da ansonsten ein compiule Fehler erschint


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass