from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request): # 요청 받으면 html  파일 경로 넣어주기 ( 상대 경로 넣어도 올바르게 처리됨 )
    return render(request, 'articles/index.html')

def introduce(request): # 요청 받으면 html  파일 경로 넣어주기 ( 상대 경로 넣어도 올바르게 처리됨 )
    return render(request, 'articles/introduce.html')

def greeting(request):
    foods = ['apple', 'banana', 'mango']
    info = {
        'name' : 'rimi'
    }
    context = {  # 하나만 보낼때도 context에 담아서 보내기, 
        'info' : info,
        'foods' : foods,
    }
    return render(request, 'articles/greeting.html',  context)  # context 자리에 {'name' : 'rimi'} 들어가도 되는데, 스타일 가이드 상 권장하지 않음 

def dinner(request):
    foods = ['pizza', 'hamburger', 'pudding', 'fries', 'potato']
    pick = random.choice(foods)
    no = ''
    context = {
        'pick' : pick,
        'foods' : foods, 
        'no' : no,
    }
    return render(request, 'articles/dinner.html', context)

def image(request):

    return render(request, 'articles/image.html')

def template_language(request):
    menus = ['짜장','짬뽕', '탕슉', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'mango', 'melon']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus, 
        'my_sentence' : my_sentence,
        'messages' : messages,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,  
    }
    return render(request, 'articles/template_language.html', context)

def throw(request):

    return render(request, 'articles/throw.html')

def catch(request):
    print(request)  # 이게 뭐야..
    print(request.GET)
    message = request.GET.get('message')
    # 사용자가 보낸 요청 -request
    # request 안에 있는 GET으로 message 받아오기 
    # ex. 냉장고가 message 면 그 요청을 받는것

    context = {
        'message':message
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name): # path('hello/<name>/', views.hello),  여기 있는 name이 넘어감
    context = {
        'name' : name
    }
    return render(request, 'articles/hello.html', context)


def homework(request):
    menus = ['m', 'e', 'n', 'u', 's']
    posts = ['zero', 'first', 'second']
    today = datetime.now()
    context = {
        'menus': menus,
        'posts' : posts,
        'today' : today
    }

    return render(request, 'articles/homework.html', context)
