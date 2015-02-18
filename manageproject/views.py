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

