from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import CustomUserCreationForm


# Create your views here.

def signup(request):
    if request.method == "POST":  # 사용자가 값을 입력했을 때, 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else: # GET 일때 => url에 접속했을 때 
        form = CustomUserCreationForm()

    context = {
        'form':form 
    }
    return render(request, 'accounts/signup.html', context)
        
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('todos:index')

    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('todos:index')