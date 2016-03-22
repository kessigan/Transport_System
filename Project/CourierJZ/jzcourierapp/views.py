from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

# Create your views here.



def sender(request):
	return render_to_response("sender.html", RequestContext(request))
	
def receiver(request):
	return render_to_response("receiver.html", RequestContext(request))