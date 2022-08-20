from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todo', views.todo, name='todo'),
    path('remove/<int:id>', views.removeTask, name='removeTask'),
    path('complete/<int:id>', views.completeTask, name='completeTask'),
    path('log', views.log, name='log'),
    path('update', views.update, name='update')
]