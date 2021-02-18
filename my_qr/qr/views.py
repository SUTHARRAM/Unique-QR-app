from django.shortcuts import render
from .forms import SoapForm
from .models import Soap

# Create your views here.

def home(request):
    context = {}
    form = SoapForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'home.html', context)

def display(request):
    soaps = Soap.objects.all()
    items = [i for i in soaps]
    context = {}
    context['items'] = items
    return render(request, 'home.html', context)
