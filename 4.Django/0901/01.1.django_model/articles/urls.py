from django.contrib import admin
from django.urls import path
from . import views

appname = 'articles'

urlpatterns = [
    path('index/', views.index),
    path(' ', views.index),  # 기본 주소 -> 지금은   http://127.0.0.1:8000/articles/  의미 
    
]
