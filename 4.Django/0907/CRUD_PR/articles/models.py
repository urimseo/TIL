from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Django가 자동으로 넣어주는 값이기 때문에 입력, 수정이 불가능 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title