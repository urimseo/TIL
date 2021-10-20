from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 사용자는 form에서 user.id를 알려준 적이 없음 
            # 하지만, article은 Foreign key에서 user_id를 넣어줘야함.'
            article = form.save(commit =False)  # 데이터가 담기긴 담기는데 아직 저장은 하지않은 상태. 저장멈춰!
            article.user = request.user         # foreign key를 login 한 유저로 채움 ( 어차피 로그인 한 사람이 글을 쓰는 사람이기 때문)
            article.save()
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
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


# @login_required
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        # 작성자만 삭제할 수 있도록 수정 
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')  # 작성자가 아닌 경우 인덱스로 
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  # db에 저장하지 않고 comment 인스턴스 객체만 반환해줌. 우리에게 시간을 주는 것 
            comment.article = article                  # 인스턴스 객
            comment.user = request.user                # 로그인한 사용자 코멘트에도 넣어주기 
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')



@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk= comment_pk)
        if request.user == comment.user:  # 로그인한 유저랑 댓글 작성자랑 같아야 삭제 가능 
            comment.delete()
    return redirect('articles:detail', article_pk)
