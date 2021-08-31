from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name = 'index'), 
    path('introduce/',views.introduce, name = 'introduce'),
    path('greeting/', views.greeting, name = 'greeting'),
    path('dinner/', views.dinner, name = 'dinner' ),
    path('image/', views.image),
    path('template_language/', views.template_language, name='template_language'),
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name = 'catch'),
    path('hello/<name>/', views.hello, name='hello'),
    # path('hello/<str:name>/', views.hello),
    # path('hello/<int:number>/', views.hello),

    path('homework/', views.homework, name='homework'),
]