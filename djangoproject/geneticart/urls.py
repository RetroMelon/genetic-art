from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.mainpage),
    url(r'^getimage', views.get_image),
)
