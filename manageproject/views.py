from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
import json 
from django.core.mail import *
from random import randrange
from datetime import datetime
# time   str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from project.models import *

from manageuser.views import *



#view all project for a given login user in unyayo 
def viewAllProject(request, user_id):

	loginUser = Users.objects.get(id = user_id)
	username = getUsername(loginUser.id)

	projects = Project_details.objects.all()

	context = {'loginUser':loginUser,'username':username,'projects':projects}
	return render(request, 'user_login_home.html',context)




#view for single selected project
def viewProject(request, user_id, project_id):

	loginUser = Users.objects.get(id = user_id)
	username = getUsername(loginUser.id)

	project = Project_details.objects.get(id = project_id)

	context = {'loginUser':loginUser,'username':username,'project':project}
	return render(request, 'single_project.html',context)



#viwe to add the project
def addProject(request, user_id):

	#checking for actual post and add new project
	if request.POST:

		#taking values form submitted form
		form = request.POST
		title = form.getlist('title_of_project')
		description = form.getlist('description_of_project')

		#saving the form for adding new project
		loginUser = Users.objects.get(id = user_id)

		newProject = Project_details()
		newProject.project_owner = loginUser
		newProject.title = title[0]
		newProject.description = description[0]
		newProject.save()



	#redirect to view for all projects
	return HttpResponseRedirect("/all-projects/" + str(user_id))


#edit infor for a given project
def editProject(request, user_id, project_id):

	#checking for actual post and edit info for a given project
	if request.POST:

		#taking values form submitted form
		form = request.POST
		title = form.getlist('edited_title_of_project')
		description = form.getlist('edited_description_of_project')

		#saving changes for a given project
		project = Project_details.objects.get(id = project_id)

		project.title = title[0]
		project.description = description[0]
		project.save()



	#redirect to view for all projects
	return HttpResponseRedirect("/project/" + str(user_id) + "/" + str(project_id))




## delete the project
def deleteProject(request, user_id, project_id):

	#checking if button is clcked
	if request.POST:

		#select the project and delete it
		project = Project_details.objects.get(id = project_id)
		project.delete()



	#redirect to view for all projects
	return HttpResponseRedirect("/all-projects/" + str(user_id))

