from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
import urllib.request
# Create your views here.


def hello(requeset):
    return HttpResponse("hello public app！")