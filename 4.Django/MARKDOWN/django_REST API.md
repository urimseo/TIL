# Django_REST API

## 1. HTTP

> HyperText Transfer Protocol

- 웹 상에서 컨텐츠를 전송하기 위한 약속 

- 웹에서 이루어지는 모든 데이터 교환의 기초
  - 요청(request)
    - 클라이언트에 의해 전송되는 메시지
  - 응답(response)
    - 서버에서 응답으로 전송되는 메시지

- 기본특성
  - Stateless
  - Connectless
- 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함



#### 1.1 HTTP request methods

- 자원에 대한 행위(수행하고자 하는 동작)을 정의
- 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
- HTTP Method 예시
  - GET, POST, PUT, DELETE

#### 1.2 HTTP response status codes

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
- 응답은 5개의 그룹으로 나뉘어짐
  1. Informational responses(1xx)
  2. Successful responses(2xx)
  3. Redirection messages(3xx)
  4. Client error responses(4xx)
  5. Server error responses(5xx)

#### 1.3 웹에서의 리소스 식별

- HTTP 요청의 대상을 리소스(resource, 자원)라고 함
- 리소스는 문서, 사진또는 기타 어떤 것이든 될 수 있음
- 각 리소스는 리소스 식별을 위해 HTTP 전체에서 사용되는 URI(Uniform Resource Identifier)로 식별됨

#### 1.4 URL, URN

- URL(Uniform Resource Locator)
  - 통합 자원 위치
  - 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
  - 과거는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성
- URN(Uniform Resource Name)
  - 통합 자원 이름
  - URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함
  - ex. ISBN(국제표준도서번호)

#### 1.5 URI

> Uniform Resource Identifier

- 통합 자원 식별자
- 인터넷의 자원을 식별하는 유일한 주소 (정보의 자원을 표현)
- 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
- 하위 개념
  - URL, URN
- URI는 크게 URL과 URN으로 나눌 수 있지만, URN을 사용하는 비중이 매우 적기 때문에 일반적으로 URL은 URI와 같은 의미처럼 사용하기도 함 

##### 1.5.1 URI의 구조

- Scheme(protocol)
  - 브라우저가 사용해야 하는 프로토콜
  - http(s), data, file, ftp, malito
  - **`https://`**www.example.com:80/path/to/myfile.html/?key=value#quick-start

- Host(Domain name)
  - 요청을 받는 웹 서버의 이름
  - IP address를 직접 사용할 수도 있지만, 실 사용시 불편하므로 웹에서 자주 사용되지는 않음 
  - ex. google의 IP address - 142.251.42.142
  - https://**`www.example.com`**:80/path/to/myfile.html/?key=value#quick-start

- PORT
  - 웹 서버 상의 리소스에 접근하는데 필요한 기술적인 '문(gate)'
  - HTTP 프로토콜의 표준 포드
    - HTTP 80
    - HTTPS 443
  - https://www.example.com**`:80`**/path/to/myfile.html/?key=value#quick-start
- Path
  - 웹 서버 상의 리소스 경로
  - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 물리적인 실제 위치가 아닌 추상화 형태의 구조로 표현
  - https://www.example.com:80**`/path/to/myfile.html`**/?key=value#quick-start
- Query(Identifier)
  - Query String Parameters
  - 웹 서버에 제공되는 추가적인 매개 변수
  - & 로 구분되는 key-value 목록
  - https://www.example.com:80/path/to/myfile.html/**`?key=value`**#quick-start
- Fragment
  - Anchor
  - 자원 안에서의 북마크의 한 종류를 나타냄
  - 브라우저에게 해당 문서(HTML)의 특정 부분을 보여주기 위한 방법
  - 브라우저에게 알려주는 요소이기 때문에 fragement identifier(부분 식별자)라고 부르며 '#' 뒤의 부분은 요청이 서버에 보내지지 않음
  - https://www.example.com:80/path/to/myfile.html/?key=value**`#quick-start`**



## 2. RESTful API

#### 2.1 API

> Application Programming Interface

- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  - 애플리케이션과 프로그래밍으로 소통하는 방법
  - CLI는 명령줄, GUI는 그래픽(아이콘), API는 프로그래밍을 통해 특정한 기능 수행
- Web API
  - 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기위해 정의된 명세
  - 현재 웹 개발은 모든 것을 직접 개발하기보다 여러 Open API를 활용하는 추세
- 응답 데이터 타입
  - HTML, XML, JSON 등
- 대표적인 API 서비스 목록
  - Youtube API, Naver Papago API, Kakao Map API ...

#### 2.2 REST

> REpresentational State Transfer

- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 2000년 로이 필딩의 박사학위 논문에서 처음으로 소개된 후 네트워킹 문화에 널리 퍼짐
- 네트워크 구조(Network Architecture)원리의 모음
  - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
- REST 원리를 따르는 시스템을 RESTful이란 용어로 지칭함

- 자원을 정의하는 방법에 대한 고민 
  - ex. 정의된 자원을 어디에 위치 시킬 것인가
- REST 자원과 주소의 지정 방법
  1. 자원
     - URI
  2. 행위
     - HTTP Method
  3. 표현
     - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된)결과물
     - JSON으로 표현된 데이터를 제공
- REST의 핵심 규칙
  1. '정보'는 URI로 표현
  2. 자원에 대한 '행위'는 HTTP Method로 표현 (GET, POST, PUT, DELETE)
- **설계 방법론은 지키지 않았을 때 잃는 것(동작 여부에 영향은 미치지 않더라도)보다 지켰을때 얻는것이 훨씬 많다!** 

#### 2.3 JSON

> JavaScript Object Notation

- JSON is lightweight data-interchange format
- JavaScript의 표기법을 따른 단순 문자열

- 특징
  - 사람이 읽거나 쓰기 쉽고 기계가 파싱(해석, 분석)하고 만들어내기 쉬움
  - 파이썬의 dictionary, 자바스크립트의 object 처럼 C계열의 언어가 갖고 있는 자료구조로 쉽게 변화할 수 있는 key-value 형태의 구조를 갖고 있음 

#### 2.4 RESTful API

- REST 원리를 따라 설계한 API!
- RESTful services, 혹은 simply REST services라고도 부름
- 프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성하자!



---

> 여기서부턴 실제 개발하면서 적용!

## 3. Response

0. 

## 4. Single Model

> 단일 모델의 data를 직렬화(serialization)하여 JSON으로 변환하는 방법.
>
>  단일 모델을 두고 CRUD 로직을 수행 가능하도록 설계하기!
>
> API 개발을 위한 핵심 기능을 제공하는 도구 활용(DRF built-in form, Postman)

<참고> Postman

- API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼
- 설계, 테스트, 문서화 등의 도구를 제공함으로써 API를 더 빠르게 개발 및 생성 할 수 있도록 도와줌

#### 1. 기본 세팅

0. 프로젝트생성 및 가상환경 세팅 등은 동일하게 진행
1.  djano-seed를 설치해준다!

`pip install django-seed`

- `INSTALLED_APPS`에 `'django_seed'`를 추가

- 개발시 테스트를 위한 fake 데이터를 생성하기 위함

  - `python manage.py seed 앱이름 --number=10` 과 같이 대량의 데이터 생성이 가능

  - `python manage.py seed articles --number=20`

    -> articles 앱에 데이터 20개 생성하기!

2. Django REST framework (DRF) 라이브러리 설치

`pip install djangorestframework`

- `INSTALLED_APPS`에 `'rest_framework'`를 추가
- Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
  - Web API란,  웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세!
- DRF의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함

```python
# settings.py  - 설치된 app 확인 
INSTALLED_APPS =[
    'articles',
    'django_seed',
    'django_extensions',
    'rest_framework',
    ...,
]
```



#### 2.  url

```python
from django import 
```

#### 3. ModelSerializer

- Model의 필드를 어떻게 '직렬화' 할 지 설정하는 것이 핵심
- 이 과정은 Django에서 Model의 필드를 설정하는 것과 동일하다. 

```python
from 
```

#### 4. view

> 'many' argument

- `many=True`
  - "Serializing multiple objects"
  - 단일 인스턴스 대신 QuerySet 등을 직렬화하기 위해서는 serializer를 인스턴스화 할 때, many=True를 키워드 인자로 전달해야함. 
  - 즉, 다수의 데이터(전체 글) 조회시 many=True!!
- Build RESTful API

> articles는 article_list | articles/<int:article_pk>는 article_detail 에서 수행 가능!

|            | GET          | POST    | PUT        | DELETE      |
| ---------- | ------------ | ------- | ---------- | ----------- |
| articles/  | 전체 글 조회 | 글 작성 |            |             |
| articles/1 | 1번 글 조회  |         | 1번글 수정 | 1번 글 삭제 |

##### 4.1  GET - Article List

> 전체 글 조회 

```
```

- api_view decrator
  - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
  - View 함수가 응답해야 하는 HTTP 메서드의 목록을 리스트의 인자로 받음
  - **DRF에서는 선택이 아닌 필수적!!!!!으로 작성해야 해당 view 함수가 정상적으로 동작한다!!**

##### 4.2 GET - Article Detail

> 특정 게시글 조회 

- Article List와 Article Detail을 구분하기 위해 추가 Serializer 정의
- 모든 필드를 직렬화 하기 위해 fields옵션을 `'__all__'`로 설정

```python
# articles/serializers.py
```

##### 4.3 POST - Create Article

> 게시글 작성

- 201 Created 상태 코드 및 메시지 응답
- RESTful 구조에 맞게 작성하기
  1. URI는 자원을 표현
  2. 자원을 조작하는 행위는 HTTP Method
- article_list 함수로 게시글을 조회하거나 생성하는 행위를 모두 처리 가능
  - 조건문으로 분기!

```python
# articles/views.py

def article_list()
```



> Status Codes in DRF

- DRF에는 status code를 보다 명확하고 읽기 쉽게 만드는 데 사용할 수 있는 정의된 상수 집합을 제공
- status 모듈에 HTTP status code 집합이 모두 포함되어 있다. 

```python
# status 모듈 예시

from rest_framework import status

def example_list(request):
    return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- 단순히 `Response(serializer.data, status=201)`로도 사용 가능! but DRF는 권장하지 않는다.

