from django.shortcuts import render
from django.http import request, HttpResponse 
# from django.views import generic


import requests
import re

from openapi.settings import OPEN_API_AUTHORIZATION


def requests_call(url=None, params=None, method='get', etc_headers=None, **kwargs):
    """
    openapi call
    """

    if(not url): return {}

    # OPEN_API_AUTHORIZATION['MAVER']
    
    # headers
    headers = {
        'X-NCP-APIGW-API-KEY-ID': OPEN_API_AUTHORIZATION['NAVER']['X-NCP-APIGW-API-KEY-ID'],
        'X-NCP-APIGW-API-KEY':  OPEN_API_AUTHORIZATION['NAVER']['X-NCP-APIGW-API-KEY'],
    }

    # 기타해드값 추가 
    if(etc_headers): 
        headers.update(etc_headers)

    # https://requests.readthedocs.io/en/master/
    request = getattr(requests, method)
    response = request(url, params=params, headers=headers, **kwargs)
    
    status_code = response.status_code
    encoding = response.encoding 

    if(status_code != requests.codes.ok): return {}

    content_type = response.headers['Content-Type']

    regex = re.compile("[^\w]*json[^\w]*")
    return response.json() if(not regex.search(content_type)) else response.content.decode(encoding)
    # return response.json() if(content_type.find('json') != -1) else response.content.decode(encoding)



# Create your views here.
def index(request):   
    return HttpResponse("Hello wrold. You're at the polls index.")    


# class Clustering(generic.DetailView):
#     template_name = 'maps/clustering.html'

# class Direction(generic.DetailView):
#     template_name = 'maps/direction.html'

# class Navi(generic.DetailView):
#     template_name = 'maps/navi.html'

def clustering(request):
    context = None
    return render(request, 'maps/clustering.html', context)

def direction(request):
    context = None
    return render(request, 'maps/direction.html', context)

def navi(request):
    context = None
    return render(request, 'maps/navi.html', context)