from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def view_test(request):
    return HttpResponse("testing")