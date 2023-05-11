from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from predictor.models import KeyWords


def index(request):
    return render(request, 'index.html')


def scrape_twitter(request):
    keywords = KeyWords.objects.all()

    return render(request, 'index.html')