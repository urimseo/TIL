# 03_Django_view_structure

> create & update view의 경우, 작성은 GET부터 하는데, 
> 구조상 조건 분기에서는 `request.method == ' POST'`를 먼저 작성하는 이유



## GET 먼저 분기 했을 때

### CASE1

```python
if request.method == 'GET':
    form = ArticleForm()
    context = {
    'form': form,
    }
    return render(request, 'articles/index.html', context)
else:
    form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        else:
            context = {
            'form': form
            }
        	return render(request, 'articles/index.html', context)
```

- 불필요한 반복이 많음 (`context`)

### CASE2

> 만약, CASE1 코드가 반복이라면.. context 를 if-else와 같은 레벨에 놔보자!

```python
if request.method =='GET':
    form = ArticleForm()
else: 
    # 하지만, GET을 제외한 나머지 메서드들(POST, PATCH, DELETE)등
    # 다른 메서드로 요청이 와도 실행되는 문제가 생긴다!
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
context = {
    'form':form
}
return render(request, 'articles/index.html', context)
```

- 다른 메서드가 실행되는 문제는 POST가 먼저와도 마찬가지!!

```python
if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
else:
	# 여기도 GET이 아닌 다른 메서드로 요청이 오면 동작 된다.
	form = ArticleForm()
context = {
	'form': form,
}
return render(request, 'articles/index.html', context)
```

- 둘다 맞는 말이지만, if문을 지나 `else`문이 실행될때의 2가지 상황을 보자.
  - `else` 문에 집중!!



- 첫번째 코드 - CASE1

```python
if request.method =='GET':
    form.ArticleForm()
else: # GET이 아닌 모든 메소드
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save() 
        return redirect('articles:index')
```

- 여기서 `else`구문은 `http method`가 GET이 아닐때(POST, PUT, DELETE등) 수행된다.



- 두번째 코드 - CASE2

```python
if request.method =='POST':
    form.ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index.html')
else:
    form = ArticleForm()
```

- 여기서 `else` 구문도 `http method`가 `POST` 가 아닌 다른 메서드가 요청이 들어와도 모두 수행된다. 



- 여기서 중요한 점은 `else` 구문이 수행될 때의 코드의 차이
- 첫번째 코드에서의 `else`는 `save()` 가 있는 즉, DB에 무언가 조작을 하는 코드이다.
- 그런데 두번째 코드에서의 `else`는 단순히 `form` 인스턴스를 생성하는 코드이다. 
- 의미론적으로 생각해보자.

> "만약 사용자가 내가 고려한 조건과 다른 method로 요청했을 때 단순히 form 인스턴스를 생성하는 코드를 수행하게 하실건가요(CASE2), 아니면 DB를 조작하는 코드를 수행하게 하실 건가요?(CASE1)"



## 실제 응답 확인

### CASE1

- POSTMAN을 통해 `CREATE URL`에 `PUT` 메서드로 요청 보낸 경우 

- `403 Forbidden`이라는 `title`과 함께 `body` 태그내용을 보면 "CSRF 검증에 실패했습니다. 요청을 중간하였습니다." 라는 문구를 확인할 수 있다.
- django는 `GET` method가 아니면 언제나 요청에서 `csrf` 검증을 시도한다. 
- 이 검증에 관한 코드는 `settings.py`에 작성되어 있음

```python
# settings.py
MIDDLEWARE = [
    ...,
    'django.middleware.csrf.CsrfViewMiddleware',
    ...,
]
```

- `PUT` 메서드 요청은 코드 상으로 `else`구문이 실행되기는 하겠지만, 
  애초에, `csrf`검증을 통과하지 못하기 때문에 `create` `view` 함수는 동작조차 못한다.



-> 만약 미들웨어 해당 코드를 주석 처리하고 다시 요청을 보낸다면????

- `csrf` 검증이 동작하지 않게 되고 코드상으로 `else` 구문이 실행되기 때문에 우리가 `GET`으로 요청을 보낸 것처럼 게시글 작성 페이지가 응답으로 오게된다.

  

### 허용되지 않은 HTTP method 처리하기

- 그런데 우연히 `csrf_token`을 맞춰서 통과를 하게 된다면 어떻게 될까? 
- 마찬가지로 게시글 작성 페이지가 렌더링 될 것
- 그래서 이것조차 방지한다고 한다면 `django`가 제공하는 `View decorators`를 사용해 완성할 수 있다.

```python
from django.views.decorator.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articels:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)
```

- 이렇게 하면 혹여나 `csrf_token`를 맞춰서 뚫었다고 해도 `create` 함수는 실행되지 않고, [ 404 method not allowed ](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/405)를 응답한다.

> **django가 현재 구조를 선택한 것과 그럴수 밖에 없는 이유**
>
> 1. POST가 아니면(GET, PUT, DELETE 등) DB 조작과 관련되지 않은 코드가 실행되도록 하기 위함
>
> 2. 검증을 통과하더라도 완벽하고 올바르게 처리할 수 있도록 데코레이터까지 사용해 적절한 응답 상태 코드까지 전달하면 끝 !





