from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils.decorators import method_decorator

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .models import Movie, Genre
from .serializers import MovieSerializer, MovieCreateSerializer, GenreSerializer

# Custom description
# https://drf-yasg.readthedocs.io/en/stable/custom_spec.html
@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="get a list of movies"
))
class MovieApiViewSet(viewsets.ModelViewSet):
    # serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['genres']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'fsk', 'duration']


    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return MovieCreateSerializer
        return MovieSerializer


class GenreApiViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    # disable pagination
    pagination_class = None