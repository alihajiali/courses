from django.conf.urls import include
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import *

app_name = "dsl_drf"


router = DefaultRouter()
books = router.register(r'publisher',
                        PublisherDocumentView,
                        basename='bookdocument')

urlpatterns = [
    re_path(r'^', include(router.urls)),
]