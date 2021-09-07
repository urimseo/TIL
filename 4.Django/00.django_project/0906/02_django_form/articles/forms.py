from django import forms
from django.forms.widgets import TextInput
from .models import Article

# form에는 TextFiled 없음 
# class ArticleForm(forms.Form):
#     REGION_A = 'sl'
#     REGION_B = 'dj'
#     REGION_C = 'gj'
#     REGION_D = 'gm'
#     REGION_E = 'bs'
#     # 이걸 choices 에 넣기 위해서 하나의 list로 만들기
#     # choices 값에 들어가는 것들은 모두 대문자로 작성해야 한다!!
#     REGION_CHOICES = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '광주'),
#         (REGION_D, '구미'),
#         (REGION_E, '부산'),
#     ]
    
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)    #widget은 formField에 할당됨.
#     region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select)

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목', # 원래는 title로 되어있음. 왜 들어있지.?? 어디서 설정한거지..?  model에서 설정한거..? 그럼 created랑 update는 어디갔어 메타데이터로 Article 다 가져왔자나...하
    #     widget=forms.TextInput(
    #         attrs={ # attribute 속성값은 딕셔너리로! 엔터 위치 조심 
    #             'class' : 'my-title',
    #             'placeholder' : 'Enter the title',
    #             'max-length' : 10, 
    #         }
    #     ),
    # )
    # content = forms.CharField(
    #     label = '내용',
    #     widget=forms.Textarea(
    #         attrs={
    #             'class' : 'my_content',
    #             'placeholder' : 'Enter the content',
    #             'rows' : 5,
    #             'cols' : 50,
    #         }
    #     )
    # )
    class Meta:
        model =Article
        # fields = ('title', 'content')
        fields = '__all__'  # 전체 가져오기! 문법이니 외우기 
        # exclude = ('title', )  # 제외하고 싶은 값 지정 왜 ... ,을 붙여야해...? tuple이라서?