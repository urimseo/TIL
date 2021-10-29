from ..models import Movie, Review, Actor
from rest_framework import serializers

# 전체 배우 목록
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)


# 단일 배우 정보  -> 출연 영화 포함 
class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies',)
        depth = 1