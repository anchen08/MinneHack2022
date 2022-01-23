from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Digital Footprint Project")

def about(request):
    return HttpResponse("About This WebApp")