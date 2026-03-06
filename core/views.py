from rest_framework import viewsets
from .models import Faculty, Teacher, News, Minor, Review
from .serializers import FacultySerializer, TeacherSerializer, NewsSerializer, MinorSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer
from .models import Slider, FacultyCard
from .serializers import SliderSerializer, FacultyCardSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class MinorViewSet(viewsets.ModelViewSet):
    queryset = Minor.objects.all()
    serializer_class = MinorSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all().order_by('order')
    serializer_class = SliderSerializer

class FacultyCardViewSet(viewsets.ModelViewSet):
    queryset = FacultyCard.objects.all()
    serializer_class = FacultyCardSerializer