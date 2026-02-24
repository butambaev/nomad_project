from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, TeacherViewSet, NewsViewSet, MinorViewSet, ReviewViewSet

router = DefaultRouter()
router.register('faculties', FacultyViewSet)
router.register('teachers', TeacherViewSet)
router.register('news', NewsViewSet)
router.register('minors', MinorViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls