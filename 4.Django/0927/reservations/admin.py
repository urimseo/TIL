from django.contrib import admin
from .models import Reservation

# Register your models here.

# Q3-1
admin.site.register(Reservation) # 관리자 페이지에서 Reservation data를 조회, 생성, 수정, 삭제 가능하도록  구현

# superuser 생성함
# id : admin
# pw : 1234