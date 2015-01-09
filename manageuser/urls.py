from django.conf.urls import patterns, url

from manageuser import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home_page'),
   
)
