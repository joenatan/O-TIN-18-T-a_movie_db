from rest_framework import viewsets


from .models import Movie, Genre
from .serializers import MovieSerializer, MovieCreateSerializer, GenreSerializer


class MovieApiViewSet(viewsets.ModelViewSet):
    # serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return MovieCreateSerializer
        return MovieSerializer


class GenreApiViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()