from django.contrib import admin
from .models import Course,Document

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title','course','uploaded_at')


