from django.urls import path
from .views import *

app_name = 'car'

urlpatterns = [
    path('', search, name='caar'),
    path('1', ali, name='caar'),
    path('2', ali2, name='caar'),
]