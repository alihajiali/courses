from typing import Pattern
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.Hello.as_view(), name='todo_view'),
    # path('<int:pk>/', views.HelloDetail.as_view(), name='detail_view'),
    path('<slug:my_slug>/', views.HelloDetail.as_view(), name='detail_view'),
    path('add/create/', views.CreateForm.as_view(), name='create_form'),
    path('add/create/form/', views.CreateAddForm.as_view(), name='create_add_form'),
    path('delete/<int:pk>/', views.DeleteTodo.as_view(), name='delete_todo'),
    path('update/<int:pk>', views.UpdateTodo.as_view(), name='update_todo'),
]