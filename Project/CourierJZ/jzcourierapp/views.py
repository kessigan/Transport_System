from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie

import authenticateUsers
import time

# Create your views here.


@ensure_csrf_cookie	
def sender(request):
	designation = "unknown"
	designation1 = []
	user_type = "sender"
		
	if("email" in request.POST and "password" in request.POST ):
		email = request.POST["email"]
		password = request.POST["password"]
	
		#check if the user that is trying to log in is an authenticated user
		is_user,designation = authenticateUsers.authenticateUser(email,password,user_type)
		print "AFTER THE DESIGNATION SCRIPT"
		print is_user
		authenticateUsers.writeVerdictToCSVFile(is_user)

	designation = authenticateUsers.readVerdictFromCSVFile()
	return render_to_response("sender.html", {"designation_loading":designation}, RequestContext(request))
	
@ensure_csrf_cookie	
def dispatcher(request):
	designation = "unknown"
	designation1 = []
	user_type = "dispatcher"
		
	if("email" in request.POST and "password" in request.POST ):
		email = request.POST["email"]
		password = request.POST["password"]
	
		#check if the user that is trying to log in is an authenticated user
		is_user,designation = authenticateUsers.authenticateUser(email,password,user_type)
		print "AFTER THE DESIGNATION SCRIPT"
		print is_user
		authenticateUsers.writeVerdictToCSVFile(is_user)

	designation = authenticateUsers.readVerdictFromCSVFile()
	return render_to_response("dispatcher.html", {"designation_loading":designation}, RequestContext(request))


@ensure_csrf_cookie		
def receiver(request):
	designation = "unknown"
	designation1 = []
	user_type = "receiver"
		
	if("email" in request.POST and "password" in request.POST ):
		email = request.POST["email"]
		password = request.POST["password"]
	
		#check if the user that is trying to log in is an authenticated user
		is_user,designation = authenticateUsers.authenticateUser(email,password,user_type)
		print "AFTER THE DESIGNATION SCRIPT"
		print is_user
		
		authenticateUsers.writeVerdictToCSVFile(is_user)

	designation = authenticateUsers.readVerdictFromCSVFile()
	
	return render_to_response("receiver.html", {"designation_loading":designation}, RequestContext(request))

@ensure_csrf_cookie		
def driver(request):
	designation = "unknown"
	designation1 = []
	user_type = "driver"
		
	if("email" in request.POST and "password" in request.POST ):
		email = request.POST["email"]
		password = request.POST["password"]
	
		#check if the user that is trying to log in is an authenticated user
		is_user,designation = authenticateUsers.authenticateUser(email,password,user_type)
		print "AFTER THE DESIGNATION SCRIPT"
		print is_user
		authenticateUsers.writeVerdictToCSVFile(is_user)

	designation = authenticateUsers.readVerdictFromCSVFile()
	print "AFTER READING FROM FILE", designation
	return render_to_response("driver.html", {"designation_loading":designation}, RequestContext(request))
	
def main(request):
	return render_to_response("main.html", RequestContext(request))

def login_sender(request):
	return render_to_response("login_sender.html", RequestContext(request))

@ensure_csrf_cookie	
def login_receiver(request):
	return render_to_response("login_receiver.html", {}, RequestContext(request))
	
	
def login_driver(request):
	return render_to_response("login_driver.html", RequestContext(request))
	
def login_ceo(request):
	return render_to_response("login_ceo.html", RequestContext(request))

#@csrf_protect
def login_dispatcher(request):
	return render_to_response("login_dispatcher.html", RequestContext(request))

