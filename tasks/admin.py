from django.contrib import admin

from .models import TaskStatus, Tag, Task

admin.site.register(TaskStatus)
admin.site.register(Tag)
admin.site.register(Task)

# Register your models here.
