from django.conf.urls import patterns, url

from manageproject import views

urlpatterns = patterns('',
    
    url(r'^all-projects/(?P<user_id>\d+)$', views.viewAllProject, name='viewAllProject'),
    url(r'^project/(?P<user_id>\d+)/(?P<project_id>\d+)$', views.viewProject, name='viewProject'),
   
)
