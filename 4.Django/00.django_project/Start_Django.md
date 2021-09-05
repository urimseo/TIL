# Django 시작하기

## 1. 가상환경 생성 및 활성화

1. 새로운 프로젝트를 만들고 vscode로 열기 

   

2. vscode에서 `Ctrl + Shift + P`로 검색창 활성화 후 Open Settings(JSON)에 하단의 내용 추가 (필수는 아니지만, 편리성을 위하여!)

```json
// settings.json

{
 ... 생략 ...,

 // Django
 "files.associations": {
   "**/*.html": "html",
   "**/templates/**/*.html": "django-html",
   "**/templates/**/*": "django-txt",
   "**/requirements{/**,*}.{txt,in}": "pip-requirements"
 },
 "emmet.includeLanguages": {
   "django-html": "html"
 }
}
```

3. 가상환경의 이름으로 venv로 생성

   `python -m venv venv`

---

4. **git ignore  생성** 

> app이나 다른 code 작성 전에 .gitignore 생성하는걸 권장 

​	4-1. git ignore 내용 검색

​	`https://www.toptal.com/developers/gitignore`에서 
​	python, Django, visual studio code, venv 등 해당하는 언어및 프레임워크 키워드 입력

​	4-2. Django_project 프로젝트에 `.gitignore`파일 생성 후, `1. `번에서 생성한 내용 붙여넣기

---

5. 가상환경 activate 시키기 

   `source venv/Scripts/activate`

   -> 오타 방지 위하여 자동완성 쓰기!

   

6. 설치 확인하기

   `pip list`

   

7. `django`가 없다면  가상환경을 켠 상태로, 장고 설치

   `source venv/Scripts/activate`

   `pip install django`

   

8. 프로젝트 생성하기 (ex.project이름이 django_intro 이면)

   `django-admin startproject django_intro .`

   -> 마지막 .을 꼭 붙여야한다!! 그래야 manage.py가 제대로 된 경로에서 설정됨 

   

9. `python manage.py runserver`  로 메인페이지 로켓 확인하기! 나오면 성공~

> 추가 
>
> 가상환경 종료 명령어 : `deactivate`

---

**프로젝트 구조** 

- `__init__.py`

  - 빈 파일
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시

- `settings.py`

  - 웹사이트의 모든 설정을 포함
  - 우리가 만드는 어떤 application이라도 등록이 되는 곳이며, static files의 위치, database 세부 설정 등이 작성

- `urls.py`

  - 사이트의 url와 view의 연결을 지정

- `wsgi.py`

  - Web Server Gateway Interface
  - 장고 어플리케이션이 웹서버와 연결 및 소통하는 것을 도움

- `asgi.py`

  - new in 3.0

  - Asynchronous Server Gateway Interface

  - 장고 어플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

    

---

## 2. Project & Application 초기 세팅

1. app 생성하기

   `python manage.py startapp articles`

   -> `articles` 라는 이름의 app을 생성한 것 

2. ★ app 등록하기 

   > 주의!!! 반드시 app을 생성후 등록해야 한다. 먼저 작성하고 등록하면 생성이 안됨.

   프로젝트폴더(django_intro)의
    `settings.py` -> `INSTALLED_APPS`에 articles app추가

   

```python
INSTALLED_APPS = [
    # django에서는 APPS을 사용할 때, 위에서부터 아래로 사용하기 때문에 순서가 중요하다. 
    #1. Local apps
    'articles',
    
    #2. Third party apps
    
    #3. Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

3. 추가설정

   - 언어및 시간 변경 

   > `settings.py`에서 `LANGUAGE_CODE`, `TIME_ZONE` 변경 후 저장. 변경사항은 서버를 재실행하면 반영된다. 

   1. `LANGUAGE_CODE = 'ko-kr'`  
      - 모든 사용자에게 제공되는 번역을 결정
      - 이 설정이 적용되려면 USE_118N이 활성화되어 있어야 함

   2. `TIME_ZONE = 'Asia/Seoul'`
      - 데이터 베이스 연결의 시간대를 나타내는 문자열 지정 
      - USE_TZ가 True 이고 이 옵션이 설정된 경우 데이터 베이스에서 날짜 시간을 읽으면, UTC 대신 새로 설정한 시간대의 인식 날짜 &시간이 반환됨
      - USE_TZ이 False인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의

   - USE_118N
     - Django의 번역 시스템을 활성화해야 하는지 여부를 지정
   - USE_L10N
     - 데이터의 지역화 된 형식(localized formating)을 기본적으로 활성화할지 여부를 지정
     - True일 경우, Django는 현재 locale의 혀식을 사용하여 숫자와 날짜를 표시

   - USE_TZ

     - datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
     - True일 경우 Django는 내부적으로 시간대 인식 날짜 / 시간을 사용 

     

## 3. 요청과 응답 (MTV)

1. URLS - urls.py

> HTTP 요청을 알맞은 view로 전달

```python
from django.contrib import admin
from django.urls import path

#articles 폴더 안에 있는 view.py !!반드시 경로 확인하고 import 할것!!
from articles import views

urlpatterns = [
    # 'index/'주소로 접속하면, views.index 함수를 실행
    path('index/', views.index),
    
    #admin 
    path('admin/', admin.site.urls),
]
```



2. View - views.py

> HTTP 요청을 수신하고 HTTP응답을 반환하는 함수 작성
> Model을 통해 요청에 맞는 필요 데이터에 접근
> Template에게 HTTP 응답 서식을 맡김 

```python
from django.shortcuts import render

# articles/view.py
def index(request):  # render,redirect의 첫번째 인자는 반드시 request
    return render(request, 'index.html')    

# 'index.html'이라는 상대주소로도 참고가 가능하다. 
```



3. Templates

> 실제 내용을 보여주는데 사용되는 파일 
> 파일의 구조나 레이아웃을 정의 (ex. HTML)
> Template 파일 경로의 기본 값은 `app`폴더 안의 `templates` 폴더로 지정되어있음. 

```html
<!-- articles/templates/index.html -->
<h1>만나서 반가워요!</h1>
```



---

## 4. 추가 명령어

#### [pip] freeze 

> 매번 프로젝트를 새로 세팅 혹은 배포할 때 pip install로 하나하나 설치 하지않고 한번에 가상환경을 세팅한하는 방법!
>
> 패키지 리스트를 한번에 저장해두고 한번에 설치가능!!

1. 패키지 리스트 저장 
   - `pip freeze > requirement.txt`

2. 리스트에 있는 패키지 설치 
   - `pip install -r requirement.txt`











