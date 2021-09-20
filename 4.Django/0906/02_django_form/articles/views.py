from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe # get방식이 아니면, 401
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    #create -> post(데이터를 받아서 작성)
    #유효성 검사 -> 빈 값을 허용하지 않음!
    if request.method =='POST':  # POST 먼저 보는 이유, 왜 get으로 확인 안하고?? -> 과연 post 일떄일까...? -> get이 아닌 다른 모든 method일때임. (put, patch, delete등 이 나왔을때도 이 코드가 동작). POST일 때에만! 
        form = ArticleForm(request.POST) # instance없이 들어가서 새로운 문서 create
        if form.is_valid(): # **만약 post 요청이 들어왔는데 유효하지 않은 요청 다음은 경로를 만들어 줘야한다. 
            article = form.save()
            return redirect('articles:detail', article.pk)
    else: # get요청 + post가 아닌 모든 method에서 빈form만 남기는 로직 넘겨주기  but decorator를 위에 require_http_method로 걸어버리면, 여기는 무조건 get만!! 올 수 있게 된다.
        form = ArticleForm()
    # 통과하지 못한 error 메세지들을  추가해서 'form'에 담아서 넘겨줌
    # 1. error메서지 포함한 form 넘기기(if isvalid 통과 못한경우 )
    # 2. 그냥 빈 form 넘겨주기 (get일때)
    context = {                                 # context가 else 밖에 있는 이유?  -> 유효성 검사 통과 못할 경우 갈 경로를 만들어 주는 것 .  유효성 검사 실패했을 때 
        'form' : form,
    }
    return render(request, 'articles/create.html', context)
    # new랑 create 합치면서 new.html -> create.html로 바꾸고 경로도 모두 create로 변경해주기  
    # method에 따라서 하는 행동 달라짐 
    # GET/articles/create => create(과거 new) 템플릿 출력   
    # POST/articles/create => 게시글 작성 
@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk) # 인자로 class와 pk가 들어감 
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST         # delete는 POST만 받아야 함. 여기서 decorator추가 할 경우     if request.method == 'POST':  구문은 이제 필요 없음. 미리 확인하기 때문 
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')
# 예전에는 -> return redirect('articles:detail', article.pk) # post가 아니면 그냥 detail로 redirect
# 변경 이후 -> http 405 코드(Method Not Allowed)를 받게 됨 




# edit과 update도 같은 역할 
# edit은 단순히 page만 조회 하도록 되어있음. 별다른 조작없어 method = get으로 처리 가능
# update는 기존 data를 조작하기 때문에 http method -> post 로 처리   
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    #update
    article = Article.objects.get(pk=pk)
    if request.method == 'POST': # 내용을 form에 넣은것 어떤 article인지는 알려줘야 함. 
        form = ArticleForm(request.POST, instance=article) # instance 에 기존 객체 article을 넣어줌 (수정 전에 기존 썼던 내용)
        if form.is_valid(): # 아까는 빈값 유효성 검사였는데 이건..무슨 유효성..?
            form.save() # instance있이 들어가기 때문에 update!!
            return redirect('articles:detail', article.pk)
    else: # edit
        form = ArticleForm(instance=article)
    #indatation 주의 
    context = {
        'article': article, #여기서 왜 article이랑 form 두개 다 불러와야 하지??????????? 수정 -> instance안에는 내용만 저장. update.html을 보면 , 데이터에 article.pk로 접근해야 하는데 이때 article이 필요하기 때문  
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
    # GET/articles/update -> 수정 페이지 렌더링
    # POST/articles/update -> 수정 로직 동작 (DB)
    
