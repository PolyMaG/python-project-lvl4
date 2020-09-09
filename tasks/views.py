from django.shortcuts import render
from django.http import HttpResponse
import rollbar
import sys


def index(request):
    try:
        return HttpResponse("Hello! This is a start page for task manager")
    except:
        rollbar.report_exc_info(sys.exc_info())

# Create your views here.
