from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views import generic


def redirect_tasks(request):
    return redirect(reverse("tasks:tasks_list_url"))


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
