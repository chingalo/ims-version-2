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
	return render(request,'home_page.html',context)


#to handle all requests for sign in into the system
def signin(request):

	context = {}
	return render(request, 'base.html', context)


#to hndle all requests for new user to be registered into new system
def signup(request):

	context = {}
	return render(request, 'base.html', context)	