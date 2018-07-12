# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from backend.services import watson_services as ws
from django.http import JsonResponse


def speech_to_text(request):
    pass

def tone(request):
    return JsonResponse({"response": ws.WatsonServices().get_tone()})
    

