from django.db.models import fields
from ..models import Movie, Review, Actor
from rest_framework import serializers


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields='__all__'
        depth = 1



    # class MovieSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Movie
    #         fields = '__all__'
    
    # content = serializers.CharField(required=False)
    # reviews = MovieSerializer(many=True, read_only=True)
    # movie_pks = serializers.ListField(write_only=True)
    # class Meta:
    #     model = Review
    #     fields = ('id', 'movies', 'movie_pks', 'title','content', 'rank',)
    #     fields = ('id', 'reviews', 'title', 'content', 'rank',)

    # def create(self, validated_data):
    #     movie_pks = validated_data.pop('movie_pks')
    #     review = Review.objects.create(**validated_data)
        
    #     for movie_pk in movie_pks:
    #         review.movies.add(movie_pk)
        
    #     return review

