import articles
from django.shortcuts import redirect, render
from .models import Article
# Create your views here.
def index(request):
    # articles = Article.objects.all()[::-1] # 파이썬으로 순서 변경하는법
    articles = Article.objects.order_by('-id') # orm으로 순서 변경
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)  # 이름공간 충돌 막기 위해서 'articles/를 붙여주는것!!! 필수 !!

def new(request):

    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title') # get방식이면 주소에 title, content가 나타나지만, post방식으로 하면 안나타난다. 
    content = request.POST.get('content')
    article = Article(title=title, content=content) # 첫번째 title은 models.py에 있는title, 두번째는 create안에서 get 해온 title 
    article.save()
    return redirect('articles:detail', article.pk)  # 상세페이지로 이동할때 pk 값 포함해야 이동가능
    # redirect 하려면 articles:index로 해야하나요..?


def detail(request, pk): #  pk를 가져오는게 variable routing!!
    article = Article.objects.get(pk = pk) # 첫번째는 db의 pk(model에 있는것) 두번쨰는 매개변수 pk
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')  # post방식일때만 삭제가 되고 
    else: # 주소창에 get 방식으로 접근하면 삭제 불가능 
        return redirect('articles:detail', article.pk)  # urls 
    
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' :article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)