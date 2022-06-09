from dataclasses import field
from .models import Genre, Movie
from rest_framework import serializers


class GenreSerializer(serializers.Serializer):
    class Meta:
        fields = ['id', 'name']


class MovieSerializer(serializers.Serializer):
    genre = GenreSerializer()

    class Meta:
        fields = ['id', 'title', 'release_year',
                  'number_in_stock', 'daily_rate', 'date_created', 'genre']
