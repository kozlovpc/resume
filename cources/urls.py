from django.urls import path
from . import views

urlpatterns = [
    path('',views.cource_list, name= 'course_list'),
    path('<int:course_id>/', views.cource_detail, name='course_detail')
]