from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from articles.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Article, Comment


# Create your views here.

# article_list에서 @api_view 를 사용하는 이유는?
# 데코레이터(@api_view)가 없으면 404에러 -> html로 보여짐
# 데코레이터(@api_view)가 있으면 404에러 -> Json으로 응답
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)                # Queryset 이 들어있음. db에 있는 데이터를 python에 쓰기 위해서 담는 것이 queryset
        serializer = ArticleListSerializer(articles, many=True)  # Json으로 만듬 (Serialization 하기) # 여러개면 무조건 many=True                                  
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # raise_exception=True는 기본적으로 문제가 있을 경우 HTTP 400 코드를 응답한다. 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 생성성공 - 201, 조회성공 - 200
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 400 - 생성안됨

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        # serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)   

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # 생성됨 알려줌 

