from rest_framework import serializers
from . models import Actors, Movies, MovieCast

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class MovieCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCast
        fields = '__all__'
        depth=1

