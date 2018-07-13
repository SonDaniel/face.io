# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from backend.services import watson_services as ws
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return JsonResponse({"response": "Welcome to Vid.io"})

@csrf_exempt
def stt(request):
    # video = request.body
    video = "media/video.mp4"
    return JsonResponse({"response": ws.WatsonServices().convert_stt(video)})
    
@csrf_exempt
def tone(request):
    data = request.POST.get("stt_text")
    return JsonResponse(ws.WatsonServices().get_tone(data))
    
def facial(request):
    return JsonResponse({"response": "No data at the moment"})
