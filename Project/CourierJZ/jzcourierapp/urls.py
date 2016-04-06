from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sender', views.sender, name='sender'),
	url(r'^receiver', views.receiver, name='receiver'),
	url(r'^login', views.login, name='login'),
	url(r'^driver', views.driver, name='driver'),
	url(r'^main', views.main, name='main'),
	url(r'^login_sender', views.login_sender, name='login_sender'),
	url(r'^login_receiver', views.login_receiver, name='login_receiver'),
#	url(r'^login_ceo', views.login_ceo, name='login_ceo'),
#	url(r'^login_driver', views.login_driver, name='login_driver'),
]