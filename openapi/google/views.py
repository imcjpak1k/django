from django.shortcuts import render
from django.http import request, HttpResponse 
from django.http import JsonResponse
import requests
import re
import logging

logger = logging.getLogger(__name__)

from openapi.settings import OPEN_API_AUTHORIZATION

# Create your views here.


# Create your views here.
def index(request):   
    logger.debug('google openpai view index')
    return HttpResponse("Hello wrold. You're at the google api index.")    

# javascript 참조사이트
# daleseo.com/google-oauth/