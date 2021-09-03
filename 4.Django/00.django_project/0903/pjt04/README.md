# 프레임워크 기반 웹 페이지 구현

## 1. 목표

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 통한 데이터 조작
- ORM(Object Relational Mapping)에 대한 이해
- 관리자 페이지를 통한 데이터 관리

## 2. 준비사항

1. 언어

- Python 3.9+ 

- Django 3.2+

2. 도구

- Visual Studio Code

- Chrome Browser

## 2. 요구사항

> 커뮤니티 서비스의 게시판 기능 개발을 위한 단계로, 영화 데이터의 생성, 조회, 수정, 삭제 가능한 어플리케이션
>
> 해당 기능은 향후 커뮤니티 서비스의 필수 기능으로 사용

1. 프로젝트 구조 

- `pjt04/`은 `startproject` 명령어로 생성되는 project 디렉토리
- `movies/`는 `startapp` 명령어로 생성되는 application 디렉토리

```python
pjt04/
    pjt04/
       __init__.py
       asgi.py
       settings.py
       urls.py
       wsgi.py
    templates/
       base.html
    movies/
       migrations/
       templates/
       		movies/
       		*.html
       __init__.py
       admin.py
       apps.py
       models.py
       test.py
       urls.py
       views.py

    manage.py
    README.md
```



---

## 4. 결과

### 1. `models.py`

>모델 클래스 이름 : `Movie`

| 필드명      | 자료형         | 설명        |
| ----------- | -------------- | ----------- |
| title       | String(<= 100) | 제목        |
| overview    | Text           | 줄거리      |
| poster_path | String(<=500)  | 포스터 경로 |
| created_at  | DateTime       | 작성일      |
| updated_at  | DateTime       | 수정일      |

```python
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

## 

### 2. `templates` >` base.html`

- 모든 HTML파일은 `base.html`을 확장(extends)하여 사용

- `base.html`은 모든 페이지가 공유하는 상단 네비게이션 바를 표시

- 네비게이션 바는 전체 영화 목록 조회 페이지와 새로운 영화 작성 페이 지로 이동할 수 있는 링크를 포함
- 해당 페이지로 이동하면 해당 네비게이션 메뉴 활성화
- 페이지 이동시 해당하는 Title도 변경 

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <title>{% block title %}{% endblock title %}</title>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark text-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="{% url 'movies:index' %}">MOVIES</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link {% block index %}{% endblock index %}" aria-current="page" href="{% url 'movies:index' %}">INDEX</a>
        </li>
        <li class="nav-item">
          <a class="nav-link {% block create %}{% endblock create %} " href="{% url 'movies:new' %}">CREATE</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
    <div class ='container'>
    {% block content %}
    {% endblock content %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>
```

>Bootstrap을 오랜만에 사용하니 개념이 많이 헷갈렸다! text-color 잊지말기!!! 
>
>css에서 사용하는 표현과 bootstrap이 살짝 다르니, 이 부분 꼭 유의해서 작성해야겠다.



---

### 3. `pjt04` > `urls.py`

> 기본 경로를 `movies`>`urls.py`에  `path('', views.index, name ='index'),` 로 설정했다. 
>
> 또한, 실제 서버 이동 시 아무것도 없는 페이지가 나오는게 살짝 번거로워 개발 편의상 이 부분도 `movies.urls` 로 `include` 하였다.
>
> 그러나, 현재 프로젝트에서는 `app`이 하나밖에 존재하지 않아 상관없지만, 2개 이상의 앱을 생성하게 된다면 반드시 제거해야한다! 

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('', include('movies.urls'))
]
```

---

### 4. `movies `

#### 4.0 `admin.py`

>위에서 정의한 모델 Movie는 관리자 페이지에서 데이터의 생성, 조회, 수정, 삭제 가능

```python
from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'overview', 'poster_path', 'created_at', 'updated_at')

admin.site.register(Movie, MovieAdmin)
```

> 까먹고 있던, class 먼저 선언 후 함수호출!! 자연스러워지도록 연습하자!



####  4.1.`views.py`

- `index` : 전체 영화 목록 조회 -> `index.html`
- `new` : 새로운 영화 작성 form  -> `new.html`
- `create` : 영화 데이터 저장
- `detail` : 단일 영화 상세 조회 -> `detail.html`
- `edit` : 단일 영화 수정 -> `edit.html`
- `update` : 수정된 영화 데이터 저장
- `delete` : 단일 영화 삭제 

```python
from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    movie = Movie(title = title, overview = overview, poster_path = poster_path)
    movie.save()
    return redirect('movies:index')

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method =="POST":
        movie.title = request.POST.get('title')
        movie.overview = request.POST.get('overview')
        movie.poster_path = request.POST.get('poster_path')
        movie.save()
    return redirect('movies:detail', movie.pk)
    
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)

```

> `edit` 부분을 작성할 때, pk가 매개변수로 전달은 되지만, return이 되지 않는 것에 있어 구현이 헷갈렸다. 
>
> 기존에는 `delete`에서만 GET으로 접근한 것에 대한 차단을 해주었는데, 만일 실제 페이지라면 `update`부분도 이러한 차단이 꼭 필요할 것 같아 추가해주었다.
>
> 페어 프로그래밍을 하면서 함수호출과 코드에 대한 다른 분의 설명을 들을 수 있어 너무 도움이 많이되었다.😁  



#### 4.2 `urls.py`

- 데이터베이스에 존재하는 모든 영화의 목록을 표시
- 사용자에게 응답으로 제공할 HTML파일은 `index.html` 
- `index.html`은 `base.html`을 확장
- `index.html`에는 적절한 HTML요소를 사용하여 제목을 표시하며, 제목을 클릭 시 해당 영화의 상세 조회 페이지로 이동

```python
from django.urls import path
from . import views
app_name ='movies'
urlpatterns = [
    path('', views.index, name ='index'),
    path('new/', views.new, name ='new'),
    path('create/', views.create, name ='create'),
    path('<int:pk>/', views.detail, name ='detail'),
    path('<int:pk>/edit/', views.edit, name ='edit'),
    path('<int:pk>/update/', views.update, name ='update'),
    path('<int:pk>/delete/', views.delete, name ='delete'),

]
```

> `urls.py`에서 가장 중요한건 오타인것같다..ㅎ

#### 4.3 templates

##### 4.4.1 `index.html`

> 전체 영화 목록 조회 (HOME)

- 데이터베이스에 존재하는 모든 영화의 목록을 표시
- 사용자에게 응답으로 제공할 HTML파일
- `index.html`은 `base.html`을 확장
- `index.html`에는 적절한 HTML요소를 사용하여 제목을 표시하며, 제목을 클릭 시 해당 영화의 상세 조회 페이지로 이동

```django
{% extends 'base.html' %}
{% block title %}
🎞Movies
{% endblock title %}

{% block index %}
active
{% endblock index %}

{% block content %}
<br>
<h1 class="text-center fw-bold">MOVIES</h1>
<br>
{% for movie in movies  %}
    <a href="{% url 'movies:detail' movie.pk %}" class="text-decoration-none text-black">{{ movie.title }}</a>
    <hr>
{% endfor %}
{% endblock content %}
```



##### 4.4.2 `detail.html`

> 단일 영화 상세 조회

- URL을 통해 함께 전달된 pk에 해당하는 영화 상세정보를 HTML에 표시
- `detail.html`은 `base.html`을 확장
- `detail.html`에는 조회하는 영화의 제목, 줄거리, 포스터 이미지를 표시

```django
{% extends 'base.html' %}
{% block title %}
🧾Detail
{% endblock title %}

{% block content %}
    <h1 class="text-center fw-bold">DETAIL</h1>

    <div class="container">
        <div class="row justify-content-center">
            <div class="card justify-content-center" style="width: 30rem;">
                <img src="{{ movie.poster_path }}" class="card-img-top" alt="...">
                <div class="card-body pb-0">
                    <h3 class="card-title fw-bold">{{ movie.title }}</h3> <hr>
                    <p class="card-text">{{ movie.overview }}</p> <hr>
                </div>
                <div class="row flex-row-reverse">
                    <p class="text-end fs-6 text-muted">작성일: {{ movie.created_at }}<br>수정일: {{ movie.updated_at }}</p>
                </div>
                <div class="row flex-row-reverse">        
                    <form action="{% url 'movies:delete' movie.pk %}" method="POST" class="col-3 d-inline-block">
                        {% csrf_token %}
                        <button class ="btn btn-danger">DELETE</button>
                    </form>    
                    <form action="{% url 'movies:edit' movie.pk %}" method="POST" class="col-2 d-inline-block">
                        {% csrf_token %}
                        <button class ="btn btn-primary">EDIT</button> 
                        <br>
                    </form>   
                </div> <br>
            </div>     
        </div> 
    </div> <br>

{% endblock content %}
```

> 처음에 포스터 이미지가 보여야한다는 걸 간과하고 지나쳐서 이후 bootstrap으로 다시 만들었다.
>
> 실제 페이지가 나오고, 이미지 링크까지 연결되니 너무 신기하고 만들면서 가장 뿌듯했던 페이지였던 것 같다!



##### 4.4.3 `new.html`

> 새로운 영화 작성 form

- 영화를 작성할 수 있는 Form을 표시하며, 다음과 같은 input 요소들을 포함

  | 필드명      | HTML 요소 | Type |
  | ----------- | --------- | ---- |
  | title       | input     | text |
  | overview    | textarea  | -    |
  | poster_path | input     | -    |

- 요청과 함께 전송된 데이터를 데이터베이스에 저장

- 저장이 완료되면 전체 영화 목록 조회 페이지로 `redirect`

```django
{% extends 'base.html' %}
{% block title %}
✨NEW
{% endblock title %}

{% block create %}
active
{% endblock create %}

{% block content %}
<h1 class="fw-bold text-center">NEW</h1>

<form action=" {% url 'movies:create' %}" method ="POST">
    {% csrf_token %}
  <div class="mb-3">
    <label for="title" class="form-label fw-bold">TITLE </label>
    <input type="text" class="form-control" id="title" name = "title">
  </div>
  <div class="mb-3">
    <label for="overview" class="form-label fw-bold">Overview</label>
    <textarea name="overview" id="overview" cols="30" rows="10" class="form-control"></textarea>
  </div>
    <label for="poster_path" class="form-label fw-bold">Poster Path </label>
    <input type="text" class="form-control" id="poster_path" name = "poster_path">
    <br>
  <button type="submit" class="btn btn-primary">작성</button>
</form>
{% endblock content %}
```



##### 4.4.4 `edit.html`

> 단일영화 정보를 수정

- 수정 요청과 함께 기존 데이터의 `pk`값을 불러옴
- 수정이 완료되면 수정한 영화의 상세 조회 페이지로 `redirect`

```django
{% extends 'base.html' %}
{% block title %}
✒Edit
{% endblock title %}

{% block content %}
<h1 class = "fw-bold text-center">EDIT</h1>
<form action=" {% url 'movies:update' movie.pk %}" method ="POST">
    {% csrf_token %}
  <div class="mb-3">
    <label for="title" class="form-label fw-bold">TITLE </label>
    <input type="text" class="form-control" id="title" name = "title" value = {{ movie.title }}>
  </div>
  <div class="mb-3">
    <label for="overview" class="form-label fw-bold">Overview</label>
    <textarea name="overview" id="overview" cols="30" rows="10" class="form-control">{{movie.overview}}</textarea>
  </div>
    <label for="poster_path" class="form-label fw-bold">Poster Path </label>
    <input type="text" class="form-control" id="poster_path" name = "poster_path" value = {{movie.poster_path}}>	
    <br>
  <button type="submit" class="btn btn-success">수정</button>
</form>

{% endblock content %}
```



