from rest_framework import routers

from .views import MovieApiViewSet

router = routers.DefaultRouter()
router.register('movies', MovieApiViewSet)


urlpatterns = router.urls