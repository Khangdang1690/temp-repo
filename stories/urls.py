from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet

router = DefaultRouter()
router.register(r'stories', StoryViewSet) #The r'stories' part sets the URL prefix for this viewset. This means that all routes for StoryViewSet will start with /stories/

urlpatterns = [
    path('', include(router.urls))
]

