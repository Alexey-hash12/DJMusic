from django.urls import path

from . import views
# Routers
from rest_framework import routers

router = routers.SimpleRouter()
router.register('music', views.MusicViewSet, basename='music')

urlpatterns = router.urls