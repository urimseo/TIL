from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    #5. create 경로로 요청이 들어옴 (POST)
    # case1. 잘못된 입력 => 사용자가 데이터 입력 
    # case 2. 올바른입력 => 사용자가 데이터 입력 
    if request.method == 'POST':
        # 1-6. 데이터가 입력된 종이를 가져옴 -> ArticlesForm을 인스턴스 (사용자 데이터 받아서)  (빈종이 + 사용자 데이터)
        # 2-6. 데이터가 입력된 종이를 가져옴 -> ArticlesForm을 인스턴스 (사용자 데이터 받아서)  (빈종이 + 사용자 데이터)
        form = ArticleForm(data = request.POST)
        # 1-7. 사용자가 입력한 데이터가 유효한지 (올바른지) 확인
        # 2-7. 사용자가 입력한 데이터가 유효한지 (올바른지) 확인
        if form.is_valid():
            # 2.8 데이터를 db에 저장한다.
            form.save()
            # 2.8 index로 리다이렉트 시켜준다 
            return redirect('articles:index')

    else: # 1. create 경로로 요청이 들어옴(GET-DB에 영향 x) -> 빈 종이 (Form) 응답 
        form = ArticleForm() # 2. ArticleForm을 인스턴스화 한다 -> 빈종이(form) 생성 ArticleForm 이라는 클래스(설계도)로 진짜 빈종이(form) 만듬 

    # 1-8 유효하지 않으니, 잘못된 데이터를 다시 입력 받기 위해서 context 에 form을 담는다. 
    context = { # 3. 사용자에게 빈 종이를 주기 위해서 context에 form을 담는다. 
        'form': form
    }
    # 4. 사용자에게 데이터를 받기 위해 빈 종이를 넘겨준다.  -> 사용자는 데이터를 입력한다. -> 전송 버튼 click  -> POST 방식으로~~
    # 1-9. 사용자에게 올바른 데이터를 받기 위해 form을 넘겨준다 
    return render(request, 'articles/create.html', context)

# @require_POST
def detail(request, pk):
    article = Article.objects.get(pk=pk) 
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method =="POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()  # article에 수정 완료된 데이터 1줄이 들어감 
            return redirect('articles:detail', article.pk)
    else: # GET요청 -> 기존 내용 담아서 
        form = ArticleForm(instance = article)
    context = {
        'article' : article,  # article.pk로 a태그에 사용하려고 
        'form' : form,
    }
    return render(request, 'articles/update.html', context)