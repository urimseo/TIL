from rest_framework import serializers
from .models import Article

# 여러개는 List로 만듬 
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        # fields =('id', 'title', )
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model=Article
        fields = '__all__'