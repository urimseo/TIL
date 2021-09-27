
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth.decorators import login_required # 로그인 데코레이터 


# Create your views here.
def index(request):
    reservaions = Reservation.objects.all()
    context = {
        'reservations': reservaions
    }
    return render(request, 'reservations/index.html', context)


@login_required # 로그인 된 사용자만 요청 보낼 수 있도록 decorator 구현 로그인 하지 않았다면 accounts/login/ 경로로 보내진다.
@require_http_methods(['GET', 'POST'])
def create(request):    
    if request.method == 'POST': # POST 방식의 요청일 때 
        form = ReservationForm(request.POST) # ReservationForm을 사용하여 구현 
        if form.is_valid(): # 데이터 유효성 검사 -> 여기서 유효성 검사 통과하지 못하면 else 로 들어가서 오류 메시지와 함께 입력 화면으로 돌아가게 된다.
            reservation = form.save() # 사용자의 글을 저장 
            return redirect('reservations:detail', reservation.pk) # /reservation/<pk> 경로로 보내기 위하여 pk값도 같이 넘겨줘야 한다.
    else: # GET 방식의 /reservations/create 요청이 들어올 경우 글을 작성할 수 있도록, 유효하지 않은 경우에도 오류 메시지와 함께 입력 화면으로 돌아간다.
        form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservations/create.html', context)

    # Q4-1

@require_safe # GET 방식의 요청이 들어올 때 
def detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk) # 존재하지 않는 pk 게시글 조회하는 경우 404 페이지 반환
    context = {
        'reservation': reservation, # pk 값에 해당하는 상세 페이지 보여주기 
    }
    return render(request, 'reservations/detail.html', context)