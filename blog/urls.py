from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^result/$', views.result, name='result'),
]