from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .form import *
import urllib.request
# Create your views here.

@login_required(login_url='/login/')
def hello(requeset):
    return HttpResponse("hello public app！")


def login_view(request):
    flag = True
    # if request.META['REMOTE_ADDR'] == 'data.icloudcare.com':
    #     user = authenticate(username='domain', password='vsi666666')
    #     login(request, user)
    #     redirect_to = request.GET.get('next')
    #     if redirect_to is None:
    #         redirect_to = '/'
    #     return HttpResponseRedirect(redirect_to)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # init_module_and_menu(user)
            # login( username = username, password = password)
            redirect_to = request.GET.get('next')
            if redirect_to is None:
                redirect_to = '/'
            login(request, user)

            return HttpResponseRedirect(redirect_to)
        else:
            flag = False
    else:
        form = LoginForm()
    return render(request, 'public/login.html', {'form': form, 'flag': flag})