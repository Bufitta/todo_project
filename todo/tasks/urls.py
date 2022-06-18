from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.category_tasks, name='category_tasks'),
    path('<slug:category_slug>/<int:pk>', views.task_detail, name='task_detail')
]