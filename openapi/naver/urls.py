from django.urls import path
from django.views.generic import RedirectView

from . import views


# namespace
app_name = 'naver'

urlpatterns = [
    path('', views.index),
    # marker clustering
    # path('clustering', views.Clustering.as_view(), name='clustering'),
    path('clustering', views.clustering, name='clustering'),
    # direction 경로탐색
    # path('direction', views.Direction.as_view(), name='direction'),
    path('direction', views.direction, name='direction'),
    # 경로탐색(marker, direction, clustering)
    # path('navi', views.Navi.as_view(), name='navi'),
    path('navi', views.navi, name='navi'),
]
