from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageFiled
from imagekit.processors import ResizeToFill


def articles_image_path(isntance, filename):
    return f'user_{isntance.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    # image = models.ImageField(upload_to=articles_image_path, blank=True)
    # image = ProcessedImageFiled(
    #     upload_to='thumbnails/',
    #     processors=[ResizeToFill(100, 50)],
    #     format='JPEG',
    #     options={'quality' : 60}
    # )
    
    image = models.ImageField(upload_to='origins/', blank=True)
    image_thumbnail = ImageSpecField(
        source = 'image',
        processors = [ResizeToFill(100, 50)],
        format = 'JPEG',
        options = { 'quality' : 90}
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



