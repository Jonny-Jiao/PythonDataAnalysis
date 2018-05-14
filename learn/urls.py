from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^pye_bar/$',views.pyecharts_bar),
    ]
