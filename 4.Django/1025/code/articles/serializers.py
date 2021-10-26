from rest_framework import serializers
from .models import Article, Comment

# 여러개는 List로 만듬 
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields =('id', 'title', )
        # fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # 
        # depth = 1 # 한단계 더 중첩된 데이터 가져옴. 현재 id 만 가져옴. 그렇기 때문에 id를 찾아서 그 안의 data를 가져오게 된다 .


class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only = True)  # read_only가 없으면계속 입력하라고 에러남. -> 이게 pk로 접근
    # models.py에서 relatedname 바꿨으면 comments(바꾼이름)로 변경해야함

    comment_set = CommentSerializer(many=True, read_only=True)  # -> Nested 버전 
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) # 댓글개수 출력
    # 첫번째 댓글 출력하는 방법
    # comment_first = serializers.CharField(source='comment_set.first', read_only=True) # 첫번째로 달린 댓글 
    comment_first = CommentSerializer(source='comment_set.first', read_only=True)

    # 만약 댓글 중 id 값이 15 이하인 댓글을 찾고 싶다면..?
    comment_filter = serializers.SerializerMethodField('less_15')
    
    def less_15(selt, article):
        qs = Comment.objects.filter(pk__lte=15, article=article) # pk가 15보다 작거나 같은 애들 
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data

    class Meta: 
        model=Article
        fields = '__all__'
        