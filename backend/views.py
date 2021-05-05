from rest_framework import viewsets


from .models import Movie
from .serializers import MovieSerializer


class MovieApiViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()