from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # 사용자 입력 / 클래스 변수
    content = models.TextField() # 사용자 입력 
    created_at = models.DateTimeField(auto_now_add=True) # Django가 자동으로 추가 
    updated_at = models.DateTimeField(auto_now= True) # 장고가 자동으로 추가 

    def __str__(self):
        return f'[{self.id}번] 제목: {self.title} / {self.content}'
    