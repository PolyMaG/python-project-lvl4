from django.shortcuts import render
# from django.http import HttpResponse
import rollbar
import sys


def index(request):
    try:
        return render(request, 'tasks/index.html')
    except:  # noqa E722
        rollbar.report_exc_info(sys.exc_info())


def my_page(request):
    try:
        return render(request, 'tasks/my_page.html')
    except:  # noqa E722
        rollbar.report_exc_info(sys.exc_info())
