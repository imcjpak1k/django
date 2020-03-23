# django intro
# Part 1: 요청과 응답
> [튜토리얼: Part 1: 요청과 응답](https://docs.djangoproject.com/ko/3.0/intro/tutorial01/ "튜토리얼: Part 1: 요청과 응답 ")

# 프로젝생성
> django-admin startproject mysite

# 앱생성
> cd mysite \
> python manage.py startapp polls

# polls/views.py view추가
```python
# polls/views.py
from django.http import request   
from django.http import HttpResponse  

# Create your views here.
def index(request):   
    return HttpResponse("Hello wrold. You're at the polls index.")    
```


# polls/urls.py 생성
```python
# polls/urls.py
from django.urls import path  \
from . import views  
urlpatterns = [   \
    path('', views.index,  name='index'), \
]
```
