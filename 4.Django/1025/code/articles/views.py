from rest_framework.decorators import api_view
from rest_framework.response import Response

from articles.serializers import ArticleListSerializer, ArticleSerializer
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Article


# Create your views here.

# article_list에서 @api_view 를 사용하는 이유는?
# 데코레이터(@api_view)가 없으면 404에러 -> html로 보여짐
# 데코레이터(@api_view)가 있으면 404에러 -> Json으로 응답
@api_view(['GET'])
def article_list(request):
    articles = get_list_or_404(Article)                # Queryset 이 들어있음. db에 있는 데이터를 python에 쓰기 위해서 담는 것이 queryset
    serializer = ArticleListSerializer(articles, many=True)  # Json으로 만듬 (Serialization 하기)
                                                # 여러개면 무조건 many=True
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)