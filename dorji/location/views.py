from django.shortcuts import render
from django.http import HttpResponse
from .models import Location

# Create your views here.
def index(request):
    locations = Location.objects.all()
    return render(request, 'location/index.html', {'locations': locations})

def detail(request, location_id):
    try:
        location = Location.objects.get(pk=location_id)
    except Location.DoesNotExist:
        return HttpResponse("Location not found.", status=404)
    return render(request, 'location/detail.html', {'location': location})