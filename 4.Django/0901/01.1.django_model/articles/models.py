from django.db import models

# Create your models here.
class Article(models.Model):
    # id 
    # id = models.AutoField(primary_key = True)

    title = models.CharField(max_length=10)  # CharField는 max_length가 필수 인자로 들어가야함  - 유효성 검증 위함 . 클래스 변수임 데이터 한줄로 ㅣ
    content = models.TextField()  #max_lengtg -> 옵션   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    # 인스턴스 변수는 -> 이런식으로 __ㅁㅁ__ 되어있는것..!? 
    # def __init__(self, name):
    #   self.name = name