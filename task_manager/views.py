import sys

import rollbar
from django.shortcuts import redirect, reverse


def redirect_tasks(request):
    try:
        return redirect(reverse('tasks:tasks_list_url'))
    except: # noqa E722
        rollbar.report_exc_info(sys.exc_info())

# Create your views here.


'''
def login(request):
    if request.method == 'GET':
        return render(request, 'login_page.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
      # check_password(username, password)
'''
