from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.

# 커스텀 User 모델 사용하기 
class User(AbstractUser):
    pass
    