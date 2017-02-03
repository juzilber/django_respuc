from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

# Create your views here.

def index(request):
	if(request.user.is_authenticated):
		return HttpResponse(status=200)


	return HttpResponse(status=404)
