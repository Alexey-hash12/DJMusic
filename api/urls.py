from django.urls import path

from . import views
# Routers
from rest_framework import routers

router = routers.SimpleRouter()
router.register('musics', views.MusicsViewSet, basename='musics')
router.register("authors", views.AuthorsViewSet, basename='authors')
router.register('albums', views.AlbumsViewSet, basename='albums')

urlpatterns = router.urls