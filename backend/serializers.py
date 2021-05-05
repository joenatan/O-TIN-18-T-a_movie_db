from rest_framework import serializers

from .models import Movie, Genre


class GenreNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreNestedSerializer(many=True)
    
    class Meta:
        model = Movie

        # Variant 1
        #fields = ['id', 'title', 'description', 'fsk', 'duration', 'genres']

        # Variate 2 (Exclude)
        #exclude = ['genres']

        # Variante 3 alles darstellen
        fields = '__all__'


class MovieCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']
