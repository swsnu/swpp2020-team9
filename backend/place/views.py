from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse

from plan.models import Plan
from .models import Place

import json

def place(request):
    if request.method == 'GET':
        place = [place for place in Place.objects.all().values()]
        return JsonResponse(place, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body.decode())
        place_name = body['name']
        place_latitude = body['latitude']
        place_longitude = body['longitude']
        #place_rep_img = request.FILES['rep_img']
        place = Place(name = place_name, latitude = place_latitude, longitude = place_longitude)
                #rep_img = place_rep_img)
        place.save()
        return HttpResponse(status = 201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def place_id(request, id=0):
    if request.method == 'GET':
        place = Place.objects.get(id=id)
        response_dict = { 'name' : place.name, 'latitude' : place.latitude, 'longitude' : place.longitude }
        return JsonResponse(response_dict, status=201)
    elif request.method == 'PUT':
        place = Place.objects.get(id=id)
        body = json.loads(request.body.decode())
        place.name = body['name']
        place.latitude = body['latitude']
        place.longitude = body['longitude']
        place.save()
        response_dict = { 'name' : place.name, 'latitude': place.latitude, 'longitude' : place.longitude }
        return JsonResponse(response_dict, status=200)
    elif request.method == 'DELETE':
        place = Place.objects.get(id=id)
        place.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['GET','PUT','DELETE'])

# Create your views here.
