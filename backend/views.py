from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie, Genre
from .serializers import MovieSerializer, MovieCreateSerializer, GenreSerializer


class MovieApiViewSet(viewsets.ModelViewSet):
    # serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['genres']
    search_fields = ['title', 'description']


    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return MovieCreateSerializer
        return MovieSerializer


class GenreApiViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()