from django.urls import path
from . import views

#list of urls supported by app
urlpatterns = [
	path("", views.index)
]