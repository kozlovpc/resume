from django.shortcuts import render, get_object_or_404
from .models import Course

def cource_list(request):
    courses = Course.objects.all()
    return render(request, 'cources/course_list.html', {'courses': courses})
def cource_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'cources/course_detail.html', {'course': course})

