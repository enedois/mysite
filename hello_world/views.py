from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def index(request):
    return HttpResponse("Home")


def about(request):
    return HttpResponse("About")


class IndexView(generic.ListView):
    template_name = "mysite/index.html"
    