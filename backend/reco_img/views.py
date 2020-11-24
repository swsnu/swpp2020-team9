from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse

from .models import Reco_img
from location.models import Location

import json

def reco_img(request):
    if request.method == 'GET':
        reco_img = [image for image in Reco_img.objects.all().values()]
        return JsonResponse(reco_img, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body.decode())
        image = body['image']
        location = body['location']
        tags = body['tags']
        reco_img = Location(image = image, location = location, tags = tags)
        reco_img.save()
        return HttpResponse(status = 201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

# Create your views here.
