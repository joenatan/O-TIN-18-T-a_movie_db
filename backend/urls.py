from rest_framework import routers

from .views import MovieApiViewSet, GenreApiViewSet

router = routers.DefaultRouter()
router.register('movies', MovieApiViewSet)
router.register('genres', GenreApiViewSet)


urlpatterns = router.urls