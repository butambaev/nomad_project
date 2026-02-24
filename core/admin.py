from django.contrib import admin
from .models import Faculty, Teacher, News, Minor, Review

admin.site.register(Faculty)
admin.site.register(Teacher)
admin.site.register(News)
admin.site.register(Minor)
admin.site.register(Review)