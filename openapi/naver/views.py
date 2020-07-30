from django.shortcuts import render
from django.http import request, HttpResponse 
from django.http import JsonResponse
# from django.views import generic
import requests
import re
import logging

logger = logging.getLogger(__name__)

from openapi.settings import OPEN_API_AUTHORIZATION


# Create your views here.
def index(request):   
    logger.debug('naver openpai view index')
    return HttpResponse("Hello wrold. You're at the polls index.")    


# class Clustering(generic.DetailView):
#     template_name = 'maps/clustering.html'

# class Direction(generic.DetailView):
#     template_name = 'maps/direction.html'

# class Navi(generic.DetailView):
#     template_name = 'maps/navi.html'

def clustering(request):
    logger.debug('clustering 페이지이동')
    context = None
    return render(request, 'maps/clustering.html', context)

def direction(request):
    logger.debug('direction 페이지이동')
    context = None
    return render(request, 'maps/direction.html', context)

def navi(request):
    logger.debug('navi 페이지이동')
    context = None
    return render(request, 'maps/driving.html', context)


def geocode(request, query):
    """
    주소로 지리정보 검색
    """
    print("주소로 주소정보 조회")

    return JsonResponse(
        http_request(
            url='https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode',
            params={
                'query': query,  # 주소
                'coordinate': None,                   # 중심좌표
            },
        )
    )


def reversegeocode(request, coords, orders):
    """
    좌표로 지리정보 검색
    """
    print("좌표로 지리정보 검색")

    return JsonResponse(
        http_request(
            url='https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc',
            params={
                'coords': coords,           # 입력_좌표
                'orders': orders,           # 변환_작업_이름
                'sourcecrs': '',            # 좌표계
                'output': 'json',           # 출력_형식
            },
        )
    )


def driving(request, start, waypoints, goal, option):
    """
    경로탐색(Direction5)
    """
    print("경로탐색")
    # print("start", start)
    # print("waypoints", waypoints)
    # print("waypoints", waypoints if(waypoints) else '')
    # print("goal", goal)

    return JsonResponse(
        http_request(
            url='https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving',
            params={
                'start': start,
                'goal': goal,
                'option': option,
                'waypoints': waypoints if(waypoints) else '',
            },
        )
    )



# @this.route('/direction5', methods=['POST'])
# def direction5():
#     """
#     map direction5
#     """
#     logger.debug("Map Direction5")
#     json_data   = request.get_json(silent=True, cache=False, force=True)

#     return http_request(
#         url='https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving',
#         params={
#             'start': json_data.get('start'),
#             'goal': json_data.get('goal'),
#             'option': json_data.get('option'),
#             'waypoints': json_data.get('waypoints'),
#         },  
#     )




def http_request(url=None, params=None, method='get', etc_headers=None, **kwargs):
    """
    openapi call
    """

    
    # print("url {url}".format(url=url))
    # print('method : '+ method)
    # print(params)
    # print("X-NCP-APIGW-API-KEY-ID {id}".format(id=OPEN_API_AUTHORIZATION['NAVER']['X-NCP-APIGW-API-KEY-ID']))
    # print("X-NCP-APIGW-API-KEY {key}".format(key=OPEN_API_AUTHORIZATION['NAVER']['X-NCP-APIGW-API-KEY']))

    if(not url): return {}
    
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

    # print('status_code {status_code}'.format(status_code=status_code))
    # print('encoding {encoding}'.format(encoding=encoding))

    if(status_code != requests.codes.ok): return {}

    content_type = response.headers['Content-Type']
    print('content_type {content_type}'.format(content_type=content_type))

    regex = re.compile("[^\w]*json[^\w]*")
    # print(regex' if(regex.search(content_type)) else 'contents')
    return response.json() if(regex.search(content_type)) else response.content.decode(encoding)