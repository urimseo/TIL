from community.forms import CommunityForm
from community.models import Community
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


@require_safe
def index(request):
    community = Community.objects.all()
    context = {
        'community': community
    }
    return render(request, 'community/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            commu = form.save()
            return redirect('community:detail', commu.pk)
    else:
        form = CommunityForm()
    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)

@require_safe
def detail(request, pk):
    commu = get_object_or_404(Community, pk=pk)
    context = {
        'commu': commu,
    }
    return render(request, 'community/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    commu = get_object_or_404(Community, pk=pk)
    if request.method == 'POST':
        form = CommunityForm(request.POST, instance=commu)
        if form.is_valid():
            form.save()
            return redirect('community:detail', commu.pk)
    else:
        form = CommunityForm(instance=commu)
    context = {
        'commu': commu,
        'form': form,
    }
    return render(request, 'community/form.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        commu = get_object_or_404(Community, pk=pk)
        commu.delete()
    return redirect('community:index')