from rest_framework import serializers
from .models import Artist, Music

# 모든 가수 정보 
class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name')


# 모든 음악 정보 
class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title')

# 상세 음악 정보 
class MusicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist')


# 상세 가수 정보 
class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count')
