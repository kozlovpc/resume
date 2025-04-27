from django.urls import path
from . import views  # Импорт представлений из текущего приложения (cite)

urlpatterns = [
    # Пример маршрута:
    path('', views.index, name='index'),
]