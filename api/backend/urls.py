import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stt/', views.stt, name='speech_to_text'),
    url(r'^tone/', views.tone, name='tone'),
    url(r'^facial/', views.facial, name='facial'),
]