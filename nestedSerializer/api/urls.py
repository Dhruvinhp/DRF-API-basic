from django.urls import path, include
from .views import SingerViewset, SongViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singer', SingerViewset, basename='singer')
router.register('song', SongViewset, basename='song')

urlpatterns = [
    path('', include(router.urls)),
]
