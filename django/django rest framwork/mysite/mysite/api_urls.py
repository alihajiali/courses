from rest_framework import routers
from home.api_views import StoryVieweset


"""way1"""
router = routers.SimpleRouter()
"""way2"""
# router = routers.DefaultRouter()
router.register('story', StoryVieweset, basename='story')