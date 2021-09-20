from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) # 이미지 파일과 같은파일 형식은 request.FILES에 들어있음 
        if form.is_valid():
            article = form.save()
            # add_message
            # messages.add_message(request, messages.INFO,'게시글 작성 완료')
            messages.info(request, '게시글 작성 완료!✌(-‿-)✌')
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

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    # messages.add_message(request, messages.error, '게시글 삭제 완료! ')
    messages.warning(request, '게시글 삭제 완료!! ¯\(ºдಠ)/¯')
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article) 
        if form.is_valid():
            form.save()
            messages.warning(request, '꧁⍢⃝꧂게시글 수정 완료!꧁⍢⃝꧂')
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,       
    }
    return render(request, 'articles/update.html', context)