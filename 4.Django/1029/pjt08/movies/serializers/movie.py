from ..models import Movie, Review, Actor
from rest_framework import serializers

# 전체 영화 목록
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title',)


# 단일 영화 정보 
class MovieSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    # models.py 에서 역참조 하는 이름을 들고 여기 이름을 지정해야함. related_name으로 설정한 이름 들고오기 ! 아니면 . _set으로 되어있다. 
    reviews = ReviewSerializer(many=True, read_only=True) 
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'reviews', 'actors', 'release_date', 'poster_path',)
