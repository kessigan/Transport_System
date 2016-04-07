from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sender', views.sender, name='sender'),
	url(r'^receiver', views.receiver, name='receiver'),
	#url(r'^login', views.login, name='login'),
	url(r'^driver', views.driver, name='driver'),
	url(r'^main', views.main, name='main'),
	url(r'^loginsender', views.login_sender, name='login_sender'),
	url(r'^loginreceiver', views.login_receiver, name='login_receiver'),
	url(r'^loginceo', views.login_ceo, name='login_ceo'),
	url(r'^logindispatcher', views.login_dispatcher, name='login_dispatcher'),
	url(r'^logindriver', views.login_driver, name='login_driver'),
	url(r'^dispatcher', views.dispatcher, name='dispatcher'),
]