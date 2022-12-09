from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CategoryViewSet, UserViewSet
from django.urls import path, include

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('tasks', TaskViewSet)
v1_router.register('categories', CategoryViewSet)
v1_router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls))
]

