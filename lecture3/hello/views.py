from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")


def tomek(request):
    return HttpResponse("Hello, Tomek")


def david(request):
    return HttpResponse("Hello, David")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize(),
    })