import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^speech_to_text/', views.speech_to_text, name='speech_to_text'),
    url(r'^tone/', views.tone, name='tone'),
]