from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Xup, Dawg!")

def profile(request):
	return ("Where'd I put that profile!?")