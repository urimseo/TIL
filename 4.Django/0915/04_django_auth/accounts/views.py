from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login   # 뷰함수의 login과 이름이 겹치기 때문에 장고의 login 함수 이름을 변경 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm
)
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm, UserChangeForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated: # 로그인된 사용자 막기 
        return redirect('articles:index')

    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 여기서 로그인 해야함!
            auth_login(request, form.get_user())  # 해킹 당할 수도 있으니 유효성 검사 통과한 form의 user를 가져옴 
            return redirect(request.GET.get('next') or 'articles:index') # next 파라미터에 대한 추가 처리 필요 
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('articles:index') 


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:  # 로그인 된 유저만 접근 가능 
        return redirect('articles:index')
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete() 
        auth_logout(request) # 탈퇴 하면서 해당 유저의 세션 데이터도 함께 지울 경우 반드시 탈퇴 후 로그아웃 순으로 처리해야함  
    return redirect('articles:index')

@login_required # 여기는 get을 처리할 수 있어서 데코레이터 같이 쓸 수 있따. delete와는 다름!
@require_http_methods(['GET', 'POST'])  # 게시글에서 가져오는 객체만 다름 나머진 똑같다 
def update(request):
    if request.method =="POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('articles:index')
    else:
        form=CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form 
    }
    return render(request, 'accounts/update.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save() # 수정하면 로그인이 풀림 -> 세션 무효화. 기존의 세션도 변경된 세션업데이트에 맞춰서 업데이트 해줘야한다.
            update_session_auth_hash(request, form.user) # 세션 변경사항 업데이트 하기. PasswordChangeFOrm의 form인스턴스 변수가 user 인스턴스 변수를 가지고 있음 
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user) # 첫번째 인자에 무조건 유저 정보가 들어가야 함 
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)


def all_users(request):
    all_users = get_user_model().objects.all()
    context = {
        'all_users' : all_users
    }
    return render(request, 'accounts/all_users.html', context)