from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View

from .forms import TaskFilter, TaskForm
from .models import Tag, Task, TaskStatus


def task_list(request):
    if request.GET.get("self_tasks") == "on":
        queryset = Task.objects.filter(creator=request.user)
    else:
        queryset = Task.objects.all()
    f = TaskFilter(request.GET, queryset)
    return render(request, "tasks/tasks_list.html", {"filter": f})


class TasksList(generic.ListView):
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks_list"

    def get_queryset(self):
        return Task.objects.all()


class TaskDetail(generic.DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class TaskCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = TaskForm()
        return render(request, "tasks/task_create.html", {"form": form})

    def post(self, request):
        bound_form = TaskForm(request.POST)
        if bound_form.is_valid():
            new_task = bound_form.save()
            new_task.creator = request.user
            new_task.save()
            return redirect("tasks:task_detail_url", new_task.id)
        return render(request, "tasks/task_create.html", {"form": bound_form})


class TaskUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    raise_exception = True
    model = Task
    fields = ["name", "description", "status", "assigned_to", "tags"]
    template_name_suffix = "_update"


class TaskDelete(LoginRequiredMixin, generic.edit.DeleteView):
    raise_exception = True
    model = Task
    template_name_suffix = "_delete"
    success_url = reverse_lazy("tasks:tasks_list_url")


class TagsList(generic.ListView):
    template_name = "tasks/tags_list.html"
    context_object_name = "tags"

    def get_queryset(self):
        return Tag.objects.all()


class TagCreate(LoginRequiredMixin, generic.edit.CreateView):
    raise_exception = True
    model = Tag
    fields = ["title"]
    template_name_suffix = "_create"


class TagUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    raise_exception = True
    model = Tag
    fields = ["title"]
    template_name_suffix = "_update"


class TagDelete(LoginRequiredMixin, generic.edit.DeleteView):
    raise_exception = True
    model = Tag
    template_name_suffix = "_delete"
    success_url = reverse_lazy("tasks:tags_list_url")


class StatusList(generic.ListView):
    template_name = "tasks/status_list.html"
    context_object_name = "status_all"

    def get_queryset(self):
        return TaskStatus.objects.all()


class UsersList(generic.ListView):
    template_name = "tasks/users_list.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.all()
