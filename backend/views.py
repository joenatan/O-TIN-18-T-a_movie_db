from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .models import Movie, Genre
from .serializers import MovieSerializer, MovieCreateSerializer, GenreSerializer

# Custom description
# https://drf-yasg.readthedocs.io/en/stable/custom_spec.html
@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="get a list of movies"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="get details of a movies"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="create a movie"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="update a movie with id ...."
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="partial update a movie with id ...."
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="remove a movie with id ...."
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