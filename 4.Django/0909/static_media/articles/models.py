from django.db import models
from imagekit import processors
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image_thumb = ProcessedImageField(
    #     blank = True,
    #     processors = [Thumbnail(200,200)],
    #     options={'quality':90},
    #     format = 'JPEG',  # 저장하는 형식 
    # ) # 썸네일 이미지를 만듬 ! (원본 이미지를 가공하여 넣기 때문에, 원본은 저장x, 썸네일만 저장)
    # # 사용자가 이미지 파일 업로드하자나요 그걸 썸네일로 바꿔서 업로드 한다구욧!!!! 
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')
    image_thumbnail = ImageSpecField(
        source = 'image',  # 원본 이미지 필드명 
        processors = [Thumbnail(200,200)],
        format = 'JPEG',
        options ={'quality' : 90}

    ) # 썸네일은 임시 데이터라서 캐시 데이터에 저장... 여음 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


# 왼쪽아래 파이썬 누르고 더하기 누르고 find 하고 위로가서 venv > Scripts> python 선택 
