import sys

import rollbar
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views import generic


def redirect_tasks(request):
    try:
        return redirect(reverse('tasks:tasks_list_url'))
    except:  # noqa E722
        rollbar.report_exc_info(sys.exc_info())


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
# Create your views here.
