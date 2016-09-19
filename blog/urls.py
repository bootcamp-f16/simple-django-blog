from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<slug>[-\w\d]+)/$', views.post, name='post')
]