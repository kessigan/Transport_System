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

#@csrf_protect
@ensure_csrf_cookie
def login(request):
	if("email" in request.POST and "password" in request.POST ):
		email = request.POST["email"]
		password = request.POST["password"]
	
		#check if the user that is trying to log in is an authenticated user
		is_user = authenticateUsers.authenticateUser(email,password)
		print(is_user)
		
	return render_to_response("login.html", RequestContext(request))