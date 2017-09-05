from django.conf.urls import url
import views
import api

urlpatterns = [
    url(r'^api/pics', api.pics),
    url(r'^', views.index),
]
