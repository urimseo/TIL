from django.db import models

CATEGORY_CHOICES = [
    ('python', '파이썬'),
    ('web', '웹'),
    ('django', '장고')
]

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    image = models.ImageField(blank = True, upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title