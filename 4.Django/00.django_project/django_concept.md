# 01. Web Framework

## 1. Django

> Django란 보안이 우수하고 유지보수가 편리한 웹사이트를 신속하게 개발하는 하도록 도움을 주는 파이썬 웹 프레임워크

- Django is a high-level python web framework that encourages rapid development and clean, pragmatic design.
- It takes care of much of the hassle of web development, so that you can focus on writing your app without needing to reinvent the wheel.

## 2. Web

- World Wide Web
- 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간



## 3. Framework

- 프로그래밍에서 특정 운영체제를 위한 응용 프로그래밍 구조를 구현하는 클래스와 라이브러리 모임 
- 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
- Application Framework라고도 함.



## 4. Web Framework

- 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함
- 동적인 웹 페이지나, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application Framework의 일종



## 5. Framework Architecture

- MVC Design Pattern (model-view-controller)
- 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
- 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음 
- Django는 MTV Pattern 이라고 함



## 6. MTV Pattern

- Model
  - 응용 프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리 (추가, 수정, 삭제)
- Template
  - 파일의 구조나 레이아웃을 정의
  - 실제 내용을 보여주는데 사용(presentation)
- View
  - HTTP요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - template에게 응답의 서식 설정을 맡김



| MVC Pattern | MTV (Django) |
| ----------- | ------------ |
| Model       | Model        |
| View        | Template     |
| Controller  | View         |



## 7. Static web page (정적 웹 페이지)

- 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
- 데이터가 변한다고 해서 화면이 변하지 않음 
- 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 으압을 보냄
- 모든 상황에서 모든 사용자에게 동일한 정보를 표시
- 일반적으로 HTML, CSS, JavaScript로 작성됨
- flat page 라고도 함



## 8. Dynamic web page (동적 웹 페이지)

- 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
- 데이터에 따라 화면이 변화함 (ex. 주식, 환율 페이지)
- 동적 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
- 서버 사이드 프로그래밍 언어 (python, java, c++등)가 사용되며 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐



---

# 02. Template

## 1. Django Template

- "데이터 표현을 제어하는 도구이자 표현에 관련된 로직"
- 사용하는 built-in-system
  - Django template language



## 2. Django Template Language(DTL)

- django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
- 단순히 Python이  HTML에 포함된 것이 아니며, 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만, 이것은 해당 python 코드로 실행되는 것이 아님 



## 3. DTL Syntax

### 3.1 Variable (변수)

`{{ variable }}`

- render()를 사용하여 `view.py`에서 정의한 변수를 `template` 파일로 넘겨 사용하는 것 
- 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
  - 공백이나 구두점 문자 또한 사용할 수 없음
- dot(.)를 사용하여 변수 속성에 접근할 수 있음 (ex. `{{ article.title }}`)

- render()의 세번째 인자로 {'key':value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 `key`에 해당하는 문자열이 `template`에서 사용 가능한 변수명이 됨.

  - ex. `context`  = { `'article'` : `article`}

    `render(request, 'index.html', context)`

### 3.2 Filters

`{{ variable|filter }}`

- 표시할 변수를 수정할 때 사용
  - ex. name 변수를 모두 소문자로 출력
    `{{ name|lower }}`

- 60개의 built-in template filter를 제공
- chained가 가능하며 일부 필터는 인자를 받기도 함
  - ex. `{{ variable|truncatewords:30 }}`

### 3.3 Tags

`{% tag %}`

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요 
  - ex. `{% if %}{% endif %}`  ,  `{% for in %}{% endfor %}`

- 약 24개의 built-in template tags를 제공
  - `empty` -> 유효성 검사



### 3.4 Comments

`{#  #}`

- `django template`에서 라인의 주석을 표현하기 위해 사용
- 아래처럼 유효하지 않은 템플릿 코드가 포함될 수 있음
  - `{# {% if ... %} text {% else %} #}`

- 한 줄 주석에만 사용할 수 있음 (줄바꿈이 허용되지 않음)
- 여러줄 주석은 `{% comment %}`와 `{% endcomment %}` 사이에 입력

#### 

## 4. 코드 작성 순서

> 데이터의 흐름에 맞추어 작성

1. `urls.py`
2. `view.py`
3. `templates`



