from django.shortcuts import render
from .views import *
# Create your views here.

def home(request):
    return render(request,'index.html')