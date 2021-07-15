from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    blog = models.ForeignKey('blogapp.Blog', on_delete=models.CASCADE, related_name = 'comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text

# class Post(models.Model):
#     blog = models.OneToOneField('blogapp.Blog', on_delete=models.CASCADE, related_name='posts')
#     author = models.CharField(max_length = 200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default = timezone.now)
