from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, TeacherViewSet, NewsViewSet, MinorViewSet, ReviewViewSet
from .views import CategoryViewSet, SubCategoryViewSet
from .views import SliderViewSet, FacultyCardViewSet

router = DefaultRouter()
router.register('faculties', FacultyViewSet)
router.register('teachers', TeacherViewSet)
router.register('news', NewsViewSet)
router.register('minors', MinorViewSet)
router.register('reviews', ReviewViewSet)
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('sliders', SliderViewSet)
router.register('faculty-cards', FacultyCardViewSet)
urlpatterns = router.urls