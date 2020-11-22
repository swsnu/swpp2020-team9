from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse

from .models import Location

import json

def location(request):
    if request.method == 'GET':
        location_all_list = [location for location in Location.objects.all().values()]
        return JsonResponse(location_all_list, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body.decode())
        location_name = body['name']
        location_latitude = body['latitude']
        location_longitude = body['longitude']
        location = Location(name = location_name, latitude = location_latitude, longitude = location_longitude)
        location.save()
        return HttpResponse(status = 201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def location_id(request, id=0):
    if request.method == 'GET':
        location = Location.objects.get(id=id)
        response_dict = { 'name' : location.name, 'latitude' : location.latitude, 'longitude' : location.longitude }
        return JsonResponse(response_dict, status=201)
    elif request.method == 'PUT':
        location = Location.objects.get(id=id)
        body = json.loads(request.body.decode())
        location.name = body['name']
        location.latitude = body['latitude']
        location.longitude = body['longitude']
        loctaion.save()
        response_dict = { 'name' : location.name, 'latitude': location.latitude, 'longitude' : location.longitude }
        return JsonResponse(response_dict, status=200)
    elif request.method == 'DELETE':
        location = Location.objects.get(id=id)
        location.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['GET','PUT','DELETE'])

# Create your views here.
