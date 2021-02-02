from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.task_list, name="tasks_list_url"),
    path("task/create/", views.TaskCreate.as_view(), name="task_create_url"),
    path("task/<int:pk>/", views.TaskDetail.as_view(), name="task_detail_url"),
    path("task/<int:pk>/update/", views.TaskUpdate.as_view(), name="task_update_url"),
    path("task/<int:pk>/delete/", views.TaskDelete.as_view(), name="task_delete_url"),
    path("tags/", views.TagsList.as_view(), name="tags_list_url"),
    path("tag/create/", views.TagCreate.as_view(), name="tag_create_url"),
    path("tag/<int:pk>/update/", views.TagUpdate.as_view(), name="tag_update_url"),
    path("tag/<int:pk>/delete/", views.TagDelete.as_view(), name="tag_delete_url"),
    path("statuses/", views.StatusList.as_view(), name="status_list_url"),
    path("users/", views.UsersList.as_view(), name="users_list_url"),
]
