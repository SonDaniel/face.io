import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^stt/', views.stt, name='speech_to_text'),
    url(r'^tone/', views.tone, name='tone'),
]