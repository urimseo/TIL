from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/',views.profile, name='profile'),  # profile은 무조건 맨 밑에 있어야 한다. -> ex. 다른 str 함수명으로 되어있는 url이 username에 걸림. (ex. update가 username으로 인식된다.)
    # <str> +/ 명시적으로 이름 붙여주는것이 좋다.
    path('follow/<int:user_pk>/', views.follow, name='follow'),
]
