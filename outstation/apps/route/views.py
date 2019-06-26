from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import OutstationRoutePage, OnRouteTouristPlaces

def like_route(request):
    route = get_object_or_404(OutstationRoutePage, id = request.POST.get('route_id'))
    is_liked = False
    if(route.likes.filter(id = request.user.id)).exists():
        route.likes.remove(request.user)
        is_liked = False
    else:
        route.likes.add(request.user)
        is_liked = True
    count = route.likes.count()
    return JsonResponse({'likes_count':count, 'is_liked':is_liked})

def amenities(request):
    route = get_object_or_404(OutstationRoutePage, id = request.GET.get('route_id'))
    place_on_route = route.on_route_places.filter(place_id = request.POST.get('place_id'))
    print(place_on_route.amenities)
