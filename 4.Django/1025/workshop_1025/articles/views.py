from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    # 모든 게시글의 id와 title을 JSON 데이터 타입으로 응답
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)
    # 새로운 게시글의 정보를 DB에 저장하고 정보를 응답 
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 400 status code를 반환하는 raise_exception 작성 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 특정 게시글의 모든 컬럼을 응답
    if request.method =='GET':
        serializer = ArticleSerializer(article)  # 모든 데이터 응답은 ArticleSerializer
        return Response(serializer.data)
    # 특정 게시글의 정보를 수정 
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 특정 게시글을 삭제 
    elif request.method =='DELETE':
        article.delete()
        data={
            'delete' : f'{article_pk}번의 게시글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    