from rest_framework import viewsets
from .models import Faculty, Teacher, News, Minor, Review
from .serializers import FacultySerializer, TeacherSerializer, NewsSerializer, MinorSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer
from .models import Slider, FacultyCard
from .serializers import SliderSerializer, FacultyCardSerializer
import requests
from rest_framework import viewsets
from .models import ContactMessage
from .serializers import ContactMessageSerializer

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


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()

        BOT_TOKEN = "8677452477:AAGBnT3i3q0nxYA9ERweqMfrPtwrgoGz5xY"
        CHAT_ID = "-1003817608226"

        text = f"""
Новая заявка с сайта:

Имя: {message.name}
Телефон: {message.phone}
Вопрос: {message.question}
Telegram: {message.telegram}
"""

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": text
        })