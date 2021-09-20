from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm
from IPython import embed


'''
가입 -> User Create
로그인 -> Session Create
로그아웃 -> Session Delete
'''
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            auth_login(request, user) # 유저 저장하고 유저 로그인하는데.... 여기는 왜 user를 따로 변수에 저장해야하는지..? UserCreationForm에는 get_user가 없다. 
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/auth_form.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method =="POST":
        form = AuthenticationForm(request, request.POST)  # 로그인을 할때는 어떤 유저인지 받아들여 줘야 하기 때문에 request도 넣어주기
        if form.is_valid():
            auth_login(request, form.get_user())  # request.user는 검증이 안되어 있다. 
            return redirect(request.GET.get('next') or 'articles:index') 
            # request.GET -> 주소, .get('next') ->  [?next=] -> 뒤의 주소가 로그인 이후 가야할 경우 
    else:
        form = AuthenticationForm()
    context={
        'form' : form
    }
    return render(request, 'accounts/auth_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method=="POST":
        form= CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form= CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save() # db에 저장 
            update_session_auth_hash(request, user) # db에 저장된 유저랑 브라우저와 일치 시키는 것 (request <- user)로... 브라우저에 sessionid와 변경된 sessionid의 해시값을 일치시켜 주는 과정
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context ={
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)