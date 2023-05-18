from django.urls import path
from . import views

urlpatterns=[
    path('',views.nothin),
    path('list/',views.todo_list),
    path('insert/',views.insert),
    path('delete/<int:todo_id>',views.delete)
]