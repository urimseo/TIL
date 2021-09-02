import articles
from django.shortcuts import render, redirect
from .models import Article

# index는 전체 게시글 불러와야해!
# 그러니까, context return 해서 보여줘~
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
# 새로운 게시글 생성은 따로 보여줄거 없어. 
# html에서 생성할 수 있게 POST 방식으로 create로 넘겨주기만 해
def new(request):
    return render(request, 'articles/new.html')

# create는 html 파일 필요 없고 생성만
# 하나의 함수에선 하나의 기능만 할 수 있어서 
# 먼저 create 함수에서 사용자의 입력을 받아 db에 저장한다 
# redirect로 def detail을 거쳐서 detail url을 응답하도록 
# redirect -> detail.html -> def detail로 간 다음에 -> 사용자가 입력한 pk 값에 해당하는 DB를 받고
# 'articles:detail"을 응답!
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article=Article(title=title, content=content)
    article.save()
    return redirect('articles:detail', article.pk)

#pk를 가져오는 것이 variable Routing
# Variable Rougint -> url주소를 변수로 사용하는것! 
#urls.py에서 <int:pk>로 변수 지정하여 여기서 인자로 받은것

def detail(request, pk):
    article=Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

# function based view / cbv class based view  - 상속...잘 이용 재사용성 높음 앗...참고로..안함
def delete(request, pk):
    article=Article.objects.get(pk=pk)
    if request.method =="POST":  #HTTP 메소드에서 POST만 삭제될 수 있도록 
        article.delete()
        return redirect('articles:index') 
    else: # get 방식일때는 삭제 안하고 상세 페이지로 이동 
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

# create랑 비슷함.
# pk값을 받아서 해당 페이지에 있는 article을 받아오는데에 차이가 있음  
def update(request, pk):  
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail' ,article.pk)