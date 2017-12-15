from django.shortcuts import render, HttpResponse

import json

import requests


# Create your views here.

def index(request):
	return HttpResponse("<h1>Git App [Built with Django]</h1>")

def profile(request):
	try:
		request = requests.get('https://api.github.com/users/wrecodde')
		print('>>> internet')
		response = json.loads(request.text)
		print(response)
	except:
		request = open('wrecodde.txt', 'r').read()
		print('>>> local storage')
		response = json.loads(request)
		print(response)
	
	return HttpResponse(response)