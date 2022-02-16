from django.urls import path
from .views import *

app_name = "new"

urlpatterns = [
    path("1/", PostViews.as_view()),
]