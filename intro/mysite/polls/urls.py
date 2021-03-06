from django.urls import path
from django.views.generic import RedirectView

from . import views

# namespace
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.IndexView.as_view(), name='list'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/register/
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('register-redirect/', views.RegisterRedirView.as_view(), name='register-redirect'),
    # path('redirect-reg', RedirectView.as_view(url='<to_view>', permanent=False), name='redirect'),
]
