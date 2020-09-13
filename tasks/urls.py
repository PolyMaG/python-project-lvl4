from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_page/', views.my_page, name='my_page'),
]
