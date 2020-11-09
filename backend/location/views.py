from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse

from .models import Location

import json

def get_location_id(request, id=0):
    if request.method == 'GET':
        location = Location.objects.get(id=id)
        response_dict = { 'name' : location.name, 'latitude' : location.latitude, 'longitude' : location.longitude }
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET'])

# Create your views here.
