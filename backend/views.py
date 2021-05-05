from rest_framework import viewsets


from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


class MovieApiViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class GenreApiViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()