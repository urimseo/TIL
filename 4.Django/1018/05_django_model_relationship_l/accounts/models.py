from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

# 대체 작업을 해야 추후 변경 가능하다. 아니면 변경 불가능.하다고 보면됨