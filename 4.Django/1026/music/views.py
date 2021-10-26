from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_list_or_404, render
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