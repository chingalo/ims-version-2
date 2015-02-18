from django.conf.urls import patterns, url

from manageuser import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home_page'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signout/(?P<user_id>\d+)$', views.signout, name='signout'),
   
)
