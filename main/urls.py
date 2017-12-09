from django.conf.urls import url

from main import views

# my app's urls

urlpatterns = [
	url(r'^/', views.index, name='index'),
	url(r'^profile', views.profile, name='profile'),
]
