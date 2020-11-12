from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate

from .models import Plan

import json

def get_plan_id(request, id=0):
    if request.method == 'GET':
        plan = Plan.objects.get(id=id)
        response_dict = {'duration' : plan.duration, 'keywords' : plan.keywords, 'like_cnt' : plan.like_cnt}
        #, 'gallery_thumbnail' : plan.gallery_thumbnail }
        return HttpResponse(json.dumps(response_dict), status=200)
    else:
        return HttpResponseNotAllowed(['GET'])

# Create your views here.
