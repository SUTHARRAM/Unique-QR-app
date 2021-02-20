from django.forms import ModelForm
from .models import *

class SoapForm(ModelForm):
    class Meta:
        model = Soap
        fields = ['name','price',]
    