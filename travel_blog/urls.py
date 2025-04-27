from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_map, name='travel-map'),
]