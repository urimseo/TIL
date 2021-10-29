from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),

    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),

    path('reviews/', views.review_list),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),

]
