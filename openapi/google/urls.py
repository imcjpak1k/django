from django.urls import path
from django.views.generic import RedirectView

from . import views


# namespace
app_name = 'google'

urlpatterns = [
    path('', views.index),
    # # marker clustering
    # # path('clustering', views.Clustering.as_view(), name='clustering'),
    # path('maps/clustering', views.clustering, name='clustering'),
    # # direction 경로탐색
    # # path('direction', views.Direction.as_view(), name='direction'),
    # path('maps/direction', views.direction, name='direction'),
    # # 경로탐색(marker, direction, clustering)
    # # path('navi', views.Navi.as_view(), name='navi'),
    # simple map
    path('maps/simple', views.simple, name='simple'),
    # # 주소로 지리정보 검색
    # path('maps/geocode/<query>', views.geocode, name='geocode'),
    # # 좌표로 지리정보 검색
    # path('maps/reversegeocode/<coords>/<orders>', views.reversegeocode, name='reversegeocode'),
    # # 경로탐색
    # path('maps/driving/<start>/<waypoints>/<goal>/<option>', views.driving, name='driving'),
]
