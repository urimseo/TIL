from django.shortcuts import render, redirect
from .models import Article  # 명시적 상대경로 사용. -> from models가 아닌  .models로 !! 


# Create your views here.
def index(request):
    # 작성한 모든 게시글을 출력
    # 1. 모든 게시글 조회   -> Article은 table.

    articles = Article.objects.all()  # 테이블에 접근하기 위한 코드 
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)



# 1. 게시글 작성페이지를 render 하는 view
def new(request):
    return render(request, 'articles/new.html')

# 사용자로부터 입력을 받은 데이터를 저장하는 view
def create(request):
    # 가장 먼저!! new 로부터 title과 content를 받아서 저장
    #GET.get을 POST.get으로 변환
    title = request.POST.get('title')  # POST 꾸러미 열어서 title 이라는 이름의 데이터를 가져와서 title에 다시 넣기    
    content = request.POST.get('content')  # new.html에서 name을 지정해줬기 때문에 접근 가능 

    # 방법1.  -> 초큼 복잡
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 방법 2  -> 앞으로이거 쓸거임!! 
    
    article = Article(title=title, content = content)
    # 데이터 유효성 검사 및 전처리 한 후 save 하게 됨 
    article.save()


    # 방법3 ->  save 전에 유효성 검사 할 수 있는 방법이 없다. 
    # Article.objects.create(title=title, content=content)




    return render(request, 'articles/create.html')




def detail(request, pk):
    pass


def delete(request, pk):
    pass


def edit(request, pk):
    pass


def update(request, pk):
    pass
