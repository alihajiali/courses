from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('test1', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
    path('test3', views.test3, name='test3'),
    path('test4/<int:id>', views.test4, name='test4'),
    path('test5/', views.test5, name='test5'),
    path('test6/<int:id>', views.test6, name='test6'),
    path('test7/<int:id>', views.test7, name='test7'),
]