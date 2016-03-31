from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sender', views.sender, name='sender'),
	url(r'^receiver', views.receiver, name='receiver'),
	url(r'^login', views.login, name='login'),
]