
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import application
from .forms import ApplicationForm
# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    candidates = application.objects.filter(
        Q(candidateName__icontains=q) |
        Q(city__icontains=q) |
        Q(state__icontains=q) |
        Q(positionAppliedFor__icontains=q) 
    )
    p = Paginator(candidates, 3)
    page_number = request.GET.get('page')
    try : 
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage : 
        page_obj = p.page(p.num_pages)

    context = {'candidates' : page_obj}
    return render(request, 'base/home.html', context)
    
def candidate(request, id):
    candidate = application.objects.get(id=id)
    context = {'candidate':candidate}
    return render(request, 'base/candidate.html', context)

def createCandidate(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/form.html', context)

def updateCandidate(request, id):
    candidate = application.objects.get(id=id)
    form = ApplicationForm(instance=candidate)

    if request.method == 'POST':
        form = ApplicationForm(request.POST , request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/form.html', context)

def deleteCandidate(request, id):
    candidate = application.objects.get(id=id)
    if request.method == 'POST':
        candidate.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'candidate':candidate})