from django.shortcuts import render



def home_page(request):

	n = 1999

	context = {'captureValue': n}
	return render(request,'home_page.html',context)
