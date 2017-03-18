from django.conf.urls import url, include
from .import views
from random import randint
x = randint(1, 9)

app_name = 'Qrious'

urlpatterns = [

    url(r'^test/$', views.test, name='test'),

    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^(?P<pk>[0-9]+)/answer/$', views.answer, name='answer'),

    url(r'^main/$', views.main, name='main'),
            ]
