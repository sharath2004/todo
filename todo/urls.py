from django.urls import path,include
from . import views
urlpatterns=[
  path('addtask/',views.addtask,name='addtask'),
  path("markasdone/<int:pk>/",views.mark_as_done,name='mark_as_done'),
  path('markasundone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
  path('edit/<int:pk>/',views.edit,name='edit'),
  path('delete/<int:pk>/',views.delete,name='delete'),
]