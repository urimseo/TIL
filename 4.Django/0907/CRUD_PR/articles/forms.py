from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'  
        # fields =['title', 'content'] # 전부 다 하나하나 적어주는걸 권장함 
        # fields = ('title', 'content')
        # exclude = ('title', ) # title 빼고 들고오겠다.! ex. 필드가 100개 있다면, title 빼고 99개가 나옴.  __all__로 가져왔을때 빼고싶은거 있을 때만 사용
        # 참고로 ('title') -> 문자열이다! , 붙여야 튜플로 사용 가능. ('title') == 'title' 