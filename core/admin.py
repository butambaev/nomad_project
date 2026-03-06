from django.contrib import admin
from .models import Faculty, Teacher, News, Minor, Review
from .models import Category, SubCategory
from .models import Slider, FacultyCard

admin.site.register(Faculty)
admin.site.register(Teacher)
admin.site.register(News)
admin.site.register(Minor)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(SubCategory)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

@admin.register(FacultyCard)
class FacultyCardAdmin(admin.ModelAdmin):
    list_display = ('name',)
