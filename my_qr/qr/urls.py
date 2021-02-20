from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('display/', display),
    path('pdf/<int:pk>/', Pdf.as_view(), name = 'qrgen'),
]