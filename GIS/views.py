from django.shortcuts import render
from .models import Mapping

# Create your views here.

def Map(request):
    GIS = {
        'title': 'Map',
        'header': 'PACI GIS',
        'content': 'Testing viewing the map',
    }
    return render(request, 'map.html', GIS)