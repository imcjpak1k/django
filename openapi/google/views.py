from django.shortcuts import render
from django.http import request, HttpResponse 
from django.http import JsonResponse
from django.conf import settings
import requests
import re
import logging

logger = logging.getLogger(__name__)


# setting 정보가져오기
open_api_auth = settings.OPEN_API_AUTHORIZATION['GOOGLE']

# Create your views here.
def index(request):   
    logger.debug('google openpai view index')
    return HttpResponse("Hello wrold. You're at the google api index.")    

def maps_index(request):   
    logger.debug('google openpai view maps_index')
    return HttpResponse("Hello wrold. maps_index")   

def maps_simple(request):   
    logger.debug('google openpai maps_simple')
    context = {
        'key' : open_api_auth['key']
    }

    return render(request, 'maps/simple.html', context)

def maps_marker(request):   
    logger.debug('google openpai maps_marker')
    context = {
        'key' : open_api_auth['key']
    }
    
    return render(request, 'maps/marker.html', context)
# javascript 참조사이트
# daleseo.com/google-oauth/
# https://developers.google.com/maps/documentation/javascript/examples/infowindow-simple
# https://developers.google.com/maps/documentation/directions/overview?_gac=1.171781524.1597229908.EAIaIQobChMInIuc9K6U6wIVBayWCh3a_Ac3EAAYASAAEgJyp_D_BwE&_ga=2.10220339.783515214.1597190683-1451775994.1595309238