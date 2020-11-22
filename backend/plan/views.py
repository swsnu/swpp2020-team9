from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate

from .models import Plan

import json

def plan(request):
    if request.method == 'GET':
        plan = [plan for plan in Plan.objects.all().values()]
        return JsonResponse(plan, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body.decode())
        plan_duration = body['duration']
        plan_keywords = body['keywords']
        plan_like_cnt = body['like_cnt']
        plan_gallery_thumbnail = body['gallery_thumbnalil']
        plan = Plan(duration = plan_duration, keywords = plan_keywords, like_cnt = plan_like_cnt, gallery_thumbnail = plan_galllery_thumbnail)
        plan.save()
        return HttpResponse(status=201)
    else:
        return HttpResponseNotAllowed(['GET','POST'])

def plan_id(request, id=0):
    if request.method == 'GET':
        plan = Plan.objects.get(id=id)
        response_dict = {'duration' : plan.duration, 'keywords' : plan.keywords, 'like_cnt' : plan.like_cnt, 'gallery_thumbnail' : plan.gallery_thumbnail }
        return JsonResponse(str(response_dict), safe=False)
    elif request.method == 'PUT':
        plan = Plan.objects.get(id=id)
        body = json.loads(request.body.decode())
        plan.duration = body['duration']
        plan.keywords = body['keywords']
        plan.like_cnt = body['like_cnt']
        plan.gallery_thumbnail = body['gallery_thumbnail']
        plan.save()
        response_dict = { 'name' : plan.name, 'latitude': plan.latitude, 'longitude' : plan.longitude }
        return JsonResponse(response_dict, status=200)
    elif request.method == 'DELETE':
        plan = Plan.objects.get(id=id)
        plan.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['GET','PUT','DELETE'])
    
# Create your views here.
