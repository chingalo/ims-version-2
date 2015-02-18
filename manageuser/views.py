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


#home page for the system when loading
def home_page(request):

	context = {}
	return render(request,'index.html',context)



#to handle all requests for sign in into the system
def signin(request):

	loginUser = ""

	if request.POST:
		#taking values
		form = request.POST
		email = form.getlist('registered_email')
		password = form.getlist('registered_password')

		user_availability = checkUser(email[0],password[0])

		if user_availability == 1:

			loginUser = Users.objects.get(e_mail = email[0])
			loginUser.login_status = "log_in"
			loginUser.save()

			username = getUsername(loginUser.id)

			#all prpjetcs for a given user
			projects = Project_details.objects.filter(project_owner = loginUser)

			context = {'loginUser':loginUser,'username':username,'projects':projects}
			return render(request, 'user_login_home.html', context)

		

	return HttpResponseRedirect('/')	


#to hndle all requests for new user to be registered into new system
def signup(request):

	context = {}
	return render(request, 'base.html', context)	



def signout(request, user_id):

	logoutUser = Users.objects.get(id = user_id)
	logoutUser.login_status = "log_out"
	logoutUser.save()

	return HttpResponseRedirect('/')




####################################### functions  for handling some actions repeatedly##################################
#checking for available users
def checkUser(email,password):

	registered_users = Users.objects.all()

	available = 0

	for registered_user in registered_users:

		if registered_user.e_mail == email and registered_user.password == password:
			available = 1


	return available

#return username
def getUsername(user_id):

	name = ""

	loginUser = Users.objects.get(id = user_id);
	namelist =  loginUser.name.split(" ")
	name = namelist[0]

	return name
	
		


