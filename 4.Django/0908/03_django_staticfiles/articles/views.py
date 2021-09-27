from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) # 이미지 파일과 같은파일 형식은 request.FILES에 들어있음 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article) # 키워드 인자는 위치인자보다 앞에 올 수 없다. reqeust.FILES가 뒤에 오려면 files=request.FILES 로 작성해야한다 
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)



'''
# settings.py

STATIC_URL = '/static/'  # static_root  에 있는 정적 파일을 참조할 때 사용할 url

# STATIC_ROOT = BASE_DIR / 'staticfiles'   

# collectstatic명령어 
python manage.py collectstatic -> statices/admin안에 css, font, img, js 파일 다 생김

# app/static/디렉토리 경로 사용 외의 추가적인 정적 파일 경로 목록을 정의하는 리스트 
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'


# 앱의 static 폴더에 정적 파일을 저장 ex> my_app/static/my_app/example.jpg
# {% load static %}
# <img src="{% static 'myapp/example.jpg %}" alt="My image">

-> articles / static/articles 안에 파일을 저장하면
<img src="{% static 'articles/sample-img-1.jpg %}" alt="sample-img">


# media file 은 유저가 업로드 하는 파일 - Pillow 라이브러리 필요 

# 이미지 크기 변경하려면 
# settings.py -> installedapps에 'imagekit', 추가하기 (pip install django-imagekit)

model field -> imagefield

# articles > models.py

from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageFiled
from imagekit.processors import ResizeToFill

# 함수 호출 할 때는 반드시 인자 2개 필요하다. 
# MEDIA_ROOT/user<PK>/경로로 <filename>  이름으로 업로드 
def articles_image_path(isntance, filename):
    return f'user_{isntance.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    # image = models.ImageField(upload_to=articles_image_path, blank=True)

    # 이건 원본 이미지를 재가공하여 저장할 때 사용하는것. 원본 아니고 썸네일!
    # imagekit을 import 한 것도 이것때문 이거 아니면 사실 할 필요 없음 
    # image = ProcessedImageFiled(
    #     upload_to='thumbnails/',
    #     processors=[ResizeToFill(100, 50)],
    #     format='JPEG',
    #     options={'quality' : 60}
    # )

    
    image = models.ImageField(upload_to='origins/', blank=True) # MEDIA_ROOT/origins/ 경로로 파일 업로드
    image_thumbnail = ImageSpecField(
        source = 'image',
        processors = [ResizeToFill(100, 50)],
        format = 'JPEG',
        options = { 'quality' : 90}
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# MEDIA_ROOT/uploads/2021/01/01 경로로 파일 업로드 
# upload = models.FileField(upload_to='uploads/%Y/%m/%d/')


#ImageField 사용하기 위해선
# 1. settings.py 에 mediaroot. mediaurl 설정
# 2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 mediaroot의 하위 경로 지정
# 3. 업로드 된 파일의 경로는 django가 제공하는 'url' 속성을 통해 얻을 수 있다. 
# <img src="{{ article.image.url }}" alt="{{ article.image }}">


# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 사용자가 업로드 한 파일을 사용자에게 실제로 제공하기 위한 url
# 업로드 된 파일의 url -> settings.MEDIA_URL
# 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT

# articles/create.html
# enctype 파일 이미지 암호화

{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}


#articles>detail.html -> 이미지 경로 불러오기

{% extends 'base.html' %}
{% load static %}

{% block content %}
  <img src="{% static 'articles/sample-img-1.png' %}" alt="sample image">

  <h2>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  {# 이미지를 넣지 않았을때 에러가 나지 않게 처리#}
  {% if article.image %}
    <img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
  {% else %}
    <img src="{% static 'images/default.png' %}" alt="default image">
  {% endif %} 

  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성시각 : {{ article.created_at }}</p>
  <p>수정시각 : {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}


# articles> views.py > create

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) # 이미지 파일과 같은파일 형식은 request.FILES에 들어있음 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


# 이미지 수정하기 -> update

# update.html
{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button>수정</button>
  </form>
  <hr> 
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}


# views.py
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article) # 키워드 인자는 위치인자보다 앞에 올 수 없다. reqeust.FILES가 뒤에 오려면 files=request.FILES 로 작성해야한다 
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


'''
