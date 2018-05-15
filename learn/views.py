from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
import urllib.request

def hello(requeset):
    return HttpResponse("hello learn app！")


def pyecharts_bar(request):
    return render(request,'learn/pye_bar.html')

