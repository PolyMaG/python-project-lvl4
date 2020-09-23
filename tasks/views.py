from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import View
import rollbar
import sys

from .forms import TaskForm, TagForm
from .models import Task, Tag

from django.contrib.auth.mixins import LoginRequiredMixin


def tasks_list(request):
    tasks_list = Task.objects.all()
    try:
        return render(
            request, 'tasks/tasks_list.html', {'tasks_list': tasks_list}
        )
    except:  # noqa E722
        rollbar.report_exc_info(sys.exc_info())


class TaskDetail(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        try:
            return render(request, 'tasks/task_detail.html', {'task': task})
        except:  # noqa E722
            rollbar.report_exc_info(sys.exc_info())


class TaskCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = TaskForm()
        return render(request, 'tasks/task_create.html', {'form': form})

    def post(self, request):
        bound_form = TaskForm(request.POST)
        if bound_form.is_valid():
            new_task = bound_form.save()
            return redirect('tasks:task_detail_url', new_task.id)
        return render(request, 'tasks/task_create.html', {'form': bound_form})


class TaskUpdate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        bound_form = TaskForm(instance=task)
        return render(
            request, 'tasks/task_update.html', {
                'form': bound_form, 'task': task}
        )

    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        bound_form = TaskForm(request.POST, instance=task)
        if bound_form.is_valid():
            new_task = bound_form.save()
            return redirect('tasks:task_detail_url', new_task.id)
        return render(
            request,
            'tasks/task_update.html',
            {'form': bound_form, 'task': task}
        )


class TaskDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        return render(request, 'tasks/task_delete.html', {'task': task})

    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        task.delete()
        return redirect(reverse('tasks:tasks_list_url'))


def tags_list(request):
    tags = Tag.objects.all()
    try:
        return render(request, 'tasks/tags_list.html', context={'tags': tags})
    except:  # noqa E722
        rollbar.report_exc_info(sys.exc_info())


class TagDetail(View):
    def get(self, request, tag_id):
        tag = get_object_or_404(Tag, pk=tag_id)
        try:
            return render(request, 'tasks/tag_detail.html', {'tag': tag})
        except:  # noqa E722
            rollbar.report_exc_info(sys.exc_info())


class TagCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = TagForm()
        try:
            return render(request, 'tasks/tag_create.html', {'form': form})
        except:  # noqa E722
            rollbar.report_exc_info(sys.exc_info())

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            try:
                return redirect('tasks:tag_detail_url', new_tag.id)
            except:  # noqa E722
                rollbar.report_exc_info(sys.exc_info())
        try:
            return render(
                request, 'tasks/tag_create.html', {'form': bound_form}
            )
        except:  # noqa E722
            rollbar.report_exc_info(sys.exc_info())


class TagUpdate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        bound_form = TagForm(instance=tag)
        return render(
            request, 'tasks/tag_update.html', {'form': bound_form, 'tag': tag}
        )

    def post(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        bound_form = TagForm(request.POST, instance=tag)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('tasks:tag_detail_url', new_tag.id)
        return render(
            request,
            'tasks/tag_update.html',
            context={'form': bound_form, 'tag': tag}
        )


class TagDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        return render(request, 'tasks/tag_delete.html', {'tag': tag})

    def post(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        tag.delete()
        return redirect(reverse('tasks:tags_list_url'))
