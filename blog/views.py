from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from blog.models import Blog1


def index(request):
    author = get_object_or_404(Blog1)
    return render(request, "blog/index.html", {'author': author})

def detail(request):
    return HttpResponse("Details")

def result(request):
    return HttpResponse("Result here")
