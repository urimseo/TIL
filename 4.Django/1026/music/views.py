from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Artist, Music
from music.serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def artist_list(request):
    # 모든 artist 조회
    if request.method == 'GET':
        artists = get_list_or_404(Artist) 
        serializer = ArtistListSerializer(artists, many =True)
        return Response(serializer.data)
    # 가수의 정보 생성
    elif request.method == 'POST':
        serializer = ArtistSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 특정 가수의 노래 정보와 노래의 개수 정보 응답
@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

# 특정 가수의 음악 정보 생성
@api_view(['POST'])
def artist_music(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 모든 음악 조회 
@api_view(['GET'])
def music_list(request):
    music = get_list_or_404(Music)
    serializer = MusicListSerializer(music, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    # 특정 음악 상세 조회
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    # 특정 음악 정보 수정
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'음악 {music_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)