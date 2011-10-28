# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def download(request):
    return render(request, 'download.html')


def screenshots(request):
    return render(request, 'screenshots.html')
