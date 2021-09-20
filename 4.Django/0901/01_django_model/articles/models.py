from django.db import models  # models 는 부모 class

# Create your models here.
class Article(models.Model): # 부모 class 상속
    # column 정의  
    # models 안에 있는 데이터 타입 정의 
    title = models.CharField(max_length=10)  # CharField -> 길이 제한 있음   
    content = models.TextField()  # TextField -> 길이제한 설정 불가능   
    create_at = models.DateTimeField(auto_now_add=True)  #created_at으로 이름변경하기 
    updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Atricle class를 -> 설계도로 바꿔서 db에 보내줘야함. 