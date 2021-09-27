from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm
from IPython import embed # 장고할때 쓰는 디버깅 툴 
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    # embed()
     
    if request.session:
        # 로그인 했을 때
        visits_num = request.session.get('visits_num', 0)   # visits_num 들고오는데, 없으면 0
        request.session['visits_num'] = visits_num + 1 # 기존에꺼에서 1 추가해서...
    else: # 로그인 안했을 때 
        visits_num = 0

    articles = Article.objects.order_by('-pk') # 최근 작성된 게시물이 위에 올 수 있도록 역정렬 
    
    context = {
        'articles': articles,
        'visits_num' : visits_num,  # 이건 그냥 몇번 방문했는지 보여주는 것 없어도 됨. 
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST) # data 없어도 됨 어차피 request.POST 가 첫번째 위치인자이기 때문. 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# @login_required -> 로그인 안한 상태에서 삭제를 하려고 하면, 로그인창으로 보냄! 로그인을 하면 다시 돌아올떄 get방식으로 보냄.! 그러나, delete는 POST만 받음...ㅠ
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
