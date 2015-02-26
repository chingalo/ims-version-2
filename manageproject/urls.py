from django.conf.urls import patterns, url

from manageproject import views

urlpatterns = patterns('',
    
    url(r'^all-projects/(?P<user_id>\d+)$', views.viewAllProject, name='viewAllProject'),
    url(r'^add-project/(?P<user_id>\d+)$', views.addProject, name='addProject'),
    url(r'^edit-project/(?P<user_id>\d+)/(?P<project_id>\d+)$', views.editProject, name='editProject'),
    url(r'^delete-project/(?P<user_id>\d+)/(?P<project_id>\d+)$', views.deleteProject, name='deleteProject'),
    url(r'^project/(?P<user_id>\d+)/(?P<project_id>\d+)$', views.viewProject, name='viewProject'),
   
)
