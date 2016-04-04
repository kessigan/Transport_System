from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie

import authenticateUsers

# Create your views here.



def sender(request):
	return render_to_response("sender.html", RequestContext(request))
	
def receiver(request):
	return render_to_response("receiver.html", RequestContext(request))
	
def driver(request):
	return render_to_response("driver.html", RequestContext(request))

#@csrf_protect
@ensure_csrf_cookie
def login(request):
	html_to_load = "login.html"
	designation = "unknown"
	designation1 = []
	
	if("email" in request.POST and "password" in request.POST ):
		email = request.POST["email"]
		password = request.POST["password"]
	
		#check if the user that is trying to log in is an authenticated user
		is_user,designation = authenticateUsers.authenticateUser(email,password)
		designation1 = [designation]
		print(is_user)
		print(designation)
		
		if designation == "driver":
			html_to_load = "receiver.html"
		elif designation == "sender":
			html_to_load = "sender.html"
			
	print html_to_load
	return render_to_response("login.html", {"designation_loading":designation1}, RequestContext(request))
	
def driver(request):
	return render_to_response("driver.html", {}, RequestContext(request))