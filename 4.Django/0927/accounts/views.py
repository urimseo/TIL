from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated: # 이미 로그인 된 유저가 signup 페이지로 접근할 경우 
        return redirect('reservations:index') #reservation 경로로 리다이렉트
    if request.method == "POST": # POST 방식의 /accounts/signup/요청이 들어올때 
        form = UserCreationForm(request.POST)
        if form.is_valid(): # 데이터의 유효성 검사 
            form.save() # 데이터 베이스에 사용자의 정보를 저장 
            return redirect('accounts:login') # 회원가입 후 /accouts/login 경로로 리다이렉트
    else:
        form = UserCreationForm() #GET으로 요청이 들어올 경우 회원가입을 할 수 있도록 보내주는 것, 유효하지 않은 경우에도 오류 메시지와 함께 입력화면으로 돌아가게 된다.
    context = {
        'form' : form    # 입력 화면으로 돌아갈 때 form을 담아서 보내줘야하기 때문에 context에 담아서 넘겨줘야 한다. 
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated: # 이미 로그인 된 유저가 login 페이지로 접근할 때에는 
        return redirect('reservations:index') # /reservations/ 경로로 리다이렉트
    if request.method =="POST": # POST 방식의 /accounts/login 요청이 들어올 경우 
        form = AuthenticationForm(request, request.POST)  # 로그인을 할때는 어떤 유저인지 받아들여 줘야 하기 때문에 request도 넣어주기
        if form.is_valid(): # 데이터의 유효성 검사 
            auth_login(request, form.get_user())  # request.user는 검증이 안되어 있다. 따라서 유효성 검사를 통과한 form에 있는 user 데이터를 넘겨줘야 한다. 
            return redirect(request.GET.get('next') or 'reservations:index') # 
            # request.GET -> 주소, .get('next') ->  [?next=] -> 뒤의 주소가 로그인 이후 가야할 경우 
    else: # 유효하지 않은 경우 오류 메세지와 함께 입력 화면으로 돌아간다. 
        form = AuthenticationForm()
    context={
        'form' : form
    }
    return render(request, 'accounts/login.html', context)



@require_POST # POST 방식의 logout 요청만 승인하도록 데코레이터로 구현
def logout(request):
    auth_logout(request) # POST 요청일 경우 세션에 저장된 로그인 정보를 삭제하도록 
    return redirect('accounts:login') # 로그아웃 이후 /accounts/login/ 경로로 리다이렉트 

