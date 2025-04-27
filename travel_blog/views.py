from django.shortcuts import render
from .models import TravelPoint

def travel_map(request):
    points = TravelPoint.objects.all()
    return render(request, 'travel_blog/map.html', {'points': points})