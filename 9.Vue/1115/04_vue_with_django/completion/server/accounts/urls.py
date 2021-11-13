from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token), # JWT 발급해주는 url
]

# https://jpadilla.github.io/django-rest-framework-jwt/