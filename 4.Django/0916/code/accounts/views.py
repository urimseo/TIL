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
            user = form.save() # 유저 자동로그인 하기 위해서 user 에 담는 것. 만약 user 자동 로그인 하지 않으려면 그냥 form.save()하면 됨
            auth_login(request, user) # 유저 저장하고 유저 로그인하는데.... 여기는 왜 user를 따로 변수에 저장해야하는지..? UserCreationForm에는 get_user가 없다. 
            return redirect('articles:index') # def 함수로 url 되어있으면 return render(request, 'accounts/index.html')로 보내기 
    else:
        form = UserCreationForm() #GET으로 요청이 들어올 경우 회원가입을 할 수 있도록 보내주는 것 
    context = {
        'form' : form
    }
    return render(request, 'accounts/auth_form.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated: # 로그인 되어 있으면 재로그인 안됨 
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
    return render(request, 'accounts/login.html', context)

# auth_form을 사용하기 위해선 auth_form.html을 따로 생성해줘야한다. auth_form



def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    if request.user.is_authenticated: # 유저가 로그인 되어있을때만
        request.user.delete() # 회원 탈퇴 가능  탈퇴하고 로그아웃도 진행해야하는디
    return redirect('articles:index')

#회원 정보 수정 
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method=="POST":
        # forms.py에서 UserChangeForm에 나오는 filed를 변경해주어야 한다. 그렇지 않으면 admin에서 접근 가능한 모든 회원 정보의 수정이 가능하기 때문.
        form= CustomUserChangeForm(request.POST, instance=request.user) # 기존의 data를 instance에 담아야지 수정이 가능
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form= CustomUserChangeForm(instance=request.user) # GET 요청이 들어올 경우에는 회원 정보 수정 페이지로 다시 보냄 
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context) # 여기도 auth_form.html 사용 가능 

# 비밀번호 변경 
@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user, request.POST) # PasswordChangeForm의 첫번쨰 인자가 user인 이유
        if form.is_valid():
            user = form.save() # db에 저장 
            update_session_auth_hash(request, user) # db에 저장된 유저랑 브라우저와 일치 시키는 것 (request <- user)로... 브라우저에 sessionid와 변경된 sessionid의 해시값을 일치시켜 주는 과정
            # 비밀번호가 변경되면 기존 세션과 회원 인증 번호가 일치하지 않게 되어 로그인 상태를 유지할 수 없기 때문에 암호가 변경되어도 로그아웃되지 않도록 새로운 passwordhash로 session을 업데이트하는 것 
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user) 
    context ={
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)

