from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    # 登录界面
    url(r'^login/$', views.login_view),
    # url(r'^auth/$',views.auth),
    url(r'^$',views.hello)
]