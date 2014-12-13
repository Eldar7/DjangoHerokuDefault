from django.conf.urls import patterns, url

from OGS import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
)