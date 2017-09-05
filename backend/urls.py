from django.conf.urls import url
import views
import api

urlpatterns = [
    url(r'^api/search_suggestions/$', api.search_suggestions),
    url(r'^api/search/$', api.search),
    url(r'^api/pics/(?P<id>[0-9]+)$', api.pic_details),
    url(r'^api/pics/$', api.pics),
    url(r'^', views.index),
]
