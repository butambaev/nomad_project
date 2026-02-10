from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, NewsViewSet

router = DefaultRouter()
router.register('faculties', FacultyViewSet)
router.register('news', NewsViewSet)

urlpatterns = router.urls
