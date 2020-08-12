from django.shortcuts import render
from django.http import request, HttpResponse 
from django.http import JsonResponse
from django.conf import settings
import requests
import re
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):   
    logger.debug('google openpai view index')
    return HttpResponse("Hello wrold. You're at the google api index.")    

def simple(request):   
    logger.debug('google openpai simple')
    # setting 정보가져오기
    open_api_auth = settings.OPEN_API_AUTHORIZATION
    context = {
        'key' : open_api_auth['GOOGLE']['key']
    }
    return render(request, 'maps/simple.html', context)
# javascript 참조사이트
# daleseo.com/google-oauth/