from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todo', views.todo, name='todo'),
    path('todo/<int:id>', views.removeTask, name='removeTask'),
    path('log', views.log, name='log'),
    path('update', views.update, name='update')
]