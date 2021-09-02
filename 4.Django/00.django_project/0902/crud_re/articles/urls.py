from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new/', views.new, name='new'),
    path('create/',views.create, name='create'),
    path('<int:pk>/', views.detail, name = 'detail'),  # http://127.0.0.1:8000/articles/1 -> pk =1 인 게시글 상세 보이도록 
    path('<int:pk>/delete/', views.delete, name='delete'),  # 1번의 delete로 들어가면 게시글이 삭제 
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    

]