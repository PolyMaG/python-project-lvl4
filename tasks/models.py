from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


def get_default_status():
    return TaskStatus.objects.get_or_create(name="new")[0]


class TaskStatus(models.Model):
    NEW = "new"
    WORK = "work"
    TEST = "test"
    DONE = "done"
    STATUS_OPTIONS = [
        (NEW, "New"),
        (WORK, "In work"),
        (TEST, "Testing"),
        (DONE, "Done"),
    ]
    name = models.CharField(
        max_length=4,
        choices=STATUS_OPTIONS,
        unique=True,
        default=NEW,
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.ForeignKey(
        TaskStatus, default=get_default_status, on_delete=models.CASCADE
    )
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="creator"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_to",
    )
    tags = models.ManyToManyField("Tag", blank=True, related_name="tasks")

    def get_absolute_url(self):
        return reverse("tasks:task_detail_url", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("tasks:tags_list_url")

    def __str__(self):
        return self.title
