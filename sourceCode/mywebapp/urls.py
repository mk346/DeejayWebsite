from django.urls import path
from .import views


urlpatterns = [
    path ('',views.home,name='home'),
    path ('mymixes',views.mixes,name='mymixes'),
    path ('services',views.services,name='services'),
    path('video',views.video,name='video'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
   


]
