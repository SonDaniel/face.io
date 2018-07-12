# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from backend.services import watson_services as ws
from django.http import JsonResponse


def stt(request):
    return JsonResponse({"response": ws.WatsonServices().convert_stt("media/video.mp4")})

def tone(request):
    return JsonResponse({"response": ws.WatsonServices().get_tone("media/video.mp4")})
    
# def byos(request);
#     pass
