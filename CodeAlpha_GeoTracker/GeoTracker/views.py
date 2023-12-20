from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.geoip2 import GeoIP2
from .models import UserLocation
from django.conf import settings

def get_user_location(request):
    user_ip_address = request.META.get('REMOTE_ADDR', '')
    g = GeoIP2()

    try:
        location_info = g.city(user_ip_address)
        longitude = location_info.get("longitude", 0.0)
        latitude = location_info.get("latitude", 0.0)

        user_location, created = UserLocation.objects.get_or_create(
            ip_address=user_ip_address,
            defaults={'location': Point(longitude, latitude, srid=4326)}
        )
        user_location.save()
    
    except Exception as e:
        location_info = {}
        user_location = None
        
    # context dictionary with the necessary data
    context = {
        'settings': settings,
        'location_info': location_info,
        'user_location': user_location,
    }


    return render(request, 'templates/user_location.html', context)