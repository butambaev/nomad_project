from rest_framework import viewsets
from .models import Faculty, Teacher, News, Minor, Review
from .serializers import FacultySerializer, TeacherSerializer, NewsSerializer, MinorSerializer, ReviewSerializer

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