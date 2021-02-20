from django.shortcuts import render
from .forms import SoapForm
from .models import Soap
from qr_code.qrcode.utils import QRCodeOptions , ContactDetail
from .utils import *
from django.template.loader import get_template
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import View

# Create your views here.

def home(request):
    context = {}
    form = SoapForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = SoapForm()
    context['form'] = form
    
    return render(request, 'home.html', context)

def display(request):
    soaps = Soap.objects.all()
    items = [i for i in soaps]
    context = {}
    context['items'] = items
    return render(request, 'display.html', context)

class Pdf(View):
    
    def get(self, request, pk):
        item = Soap.objects.get(pk=pk)
        today = timezone.now()
        params = {
            'today': today,
            'item' : item,
            'request': request
        }
        pdf = render_to_pdf('generate_qr_pdf.html', params)
        return HttpResponse(pdf, content_type='application/pdf')
