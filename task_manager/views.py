import sys

import rollbar
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    try:
        return render(request, 'index.html')
    except:
        rollbar.report_exc_info(sys.exc_info())

# Create your views here.
