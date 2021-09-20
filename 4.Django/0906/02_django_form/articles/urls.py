from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), # GET/POST 
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'), # GET/POST
]
    # path('new/', views.new, name='new'), 하나로 합쳐서 이제 필요 없어짐 
    # path('<int:pk>/edit/', views.edit, name='edit'),