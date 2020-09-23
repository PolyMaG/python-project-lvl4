from django.db import models


class TaskStatus(models.Model):
    NEW = 'NEW'
    WORK = 'WORK'
    TEST = 'TEST'
    DONE = 'DONE'
    STATUS_OPTIONS = [
        (NEW, 'New'),
        (WORK, 'In work'),
        (TEST, 'Testing'),
        (DONE, 'Done'),
    ]
    status_name = models.CharField(
        max_length=4,
        choices=STATUS_OPTIONS,
        default=NEW,
    )

    def __str__(self):
        return self.status_name


class Task(models.Model):
    NEW = 'NEW'
    WORK = 'WORK'
    TEST = 'TEST'
    DONE = 'DONE'
    STATUS_OPTIONS = [
        (NEW, 'New'),
        (WORK, 'In work'),
        (TEST, 'Testing'),
        (DONE, 'Done'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=4,
        choices=STATUS_OPTIONS,
        default=NEW,
    )
    creator = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
# Create your models here.
