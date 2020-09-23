from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.tasks_list, name='tasks_list_url'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create_url'),
    path('task/<int:task_id>/',
         views.TaskDetail.as_view(),
         name='task_detail_url'),
    path('task/<int:task_id>/update/',
         views.TaskUpdate.as_view(),
         name='task_update_url'),
    path('task/<int:task_id>/delete/',
         views.TaskDelete.as_view(), name='task_delete_url'),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('tag/create/', views.TagCreate.as_view(), name='tag_create_url'),
    path('tag/<int:tag_id>/',
         views.TagDetail.as_view(),
         name='tag_detail_url'),
    path('tag/<int:tag_id>/update/',
         views.TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<int:tag_id>/delete/',
         views.TagDelete.as_view(), name='tag_delete_url'),
]
