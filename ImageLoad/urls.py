from django.conf.urls import url
from ImageLoad import views

urlpatterns=[
	url(r'^list/$', views.ilist, name='list')
	]