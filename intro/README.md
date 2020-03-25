# django intro
# Part 1: 요청과 응답
> [튜토리얼: Part 1: 요청과 응답](https://docs.djangoproject.com/ko/3.0/intro/tutorial01/ "튜토리얼: Part 1: 요청과 응답 ")

# 프로젝생성
> django-admin startproject mysite

# 앱생성
> cd mysite 
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
from django.urls import path  
from . import views  
urlpatterns = [   
    path('', views.index,  name='index'), 
]
```


 # Part 2: 모델과 관리자 페이지
> [Part 2: 모델과 관리자 페이지](https://docs.djangoproject.com/ko/3.0/intro/tutorial02/ "Part 2: 모델과 관리자 페이지")

# DATABASE
[DATABSE 문서](https://docs.djangoproject.com/ko/3.0/ref/settings/#std:setting-DATABASES "Settings") 

```python
# mysite/setting.py
# [sqlite]
DATABASES = { 
    'default': {  
        'ENGINE': 'django.db.backends.sqlite3',   
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),    
    }
}

# mysql
DATABASES = { 
    'default': {  
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'testdb'
        'USER': 'mydatabaseuser',   
        'PASSWORD': 'mypassword',   
        'HOST': '127.0.0.1',    
        'PORT': '5432', 
    }
}
```
# TIME_ZONE
[Django timezone 문제 파헤치기](https://8percent.github.io/2017-05-31/django-timezone-problem/ "Django timezone 문제 파헤치기") 

```python
# mysite/setting.py
# TIMEZONE -> 사용자의 timezone을 받아서 계산해야함 (default)
TIME_ZONE = 'UTC'
USE_TZ = True

# TIMEZONE -> datetime.datetime.now()가 아니라 django.utils.timezone.now() 사용해야함
TIME_ZONE = 'Asia/Seoul'
USE_TZ = True 
```

# 데이터베이스 및 테이블생성 
> python manage.py migrate

# 모델만들기
```python
# polls/models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

```

# 모델활성화
 - 이 앱을 위한 스키마생성(테이블생성)
 - python 데이터베이스 접근 API생성  
  
> python manage.py migrate

```cmd
(twoscoopsofdjango) c:\Users\imcjp\workspace\vscode\django_intro\mysite>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK

(twoscoopsofdjango) c:\Users\imcjp\workspace\vscode\django_intro\mysite>
```


## INSTALLED_APPS
```python
# mysite/settings.py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
# makemigrations
 - makemigrations 을 실행함으로 모델정보 변경
 - 변경하고자 하는 내용 확인
  
> python manage.py makemigrations polls
  
```
(twoscoopsofdjango) c:\Users\imcjp\workspace\vscode\django_intro\mysite>python manage.py makemigrations polls
Migrations for 'polls':
  polls\migrations\0001_initial.py
    - Create model Question
    - Create model Choice

(twoscoopsofdjango) c:\Users\imcjp\workspace\vscode\django_intro\mysite>
```

> python manage.py sqlmigrate polls 0001

```sql
#(twoscoopsofdjango) c:\Users\imcjp\workspace\vscode\django_intro\mysite>python manage.py sqlmigrate polls 0001
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

# mirgrate
- 반영되지 않은 모델정보를 수집 및 반영하여, 모델의 변경사항과 데이터베이스의 스키마를 동기화를 진행한다.
- makemigrations으로 변경한 모델정보를 반영
  
> python manage.py migrate
> 
```
(twoscoopsofdjango) c:\Users\imcjp\workspace\vscode\django_intro\mysite>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK

(twoscoopsofdjango) c:\Users\imcjp\workspace\vscode\django_intro\mysite>
```

# 대화식 python shell
> python manage.py shell

# 관리자생성
> python manage.py createsuperuser
> 

```
(twoscoopsofdjango) c:\Users\imcjp\workspace\vscode\django\intro\mysite>python manage.py createsuperuser
Username (leave blank to use 'imcjp'): admin
Email address: admin@xx.com
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
```

> python manage.py runserver
> 
> url : http://127.0.0.1:8000/admin/

# polls app 관리자사이트 추가
```python
# polls/admin.py
from django.contrib import admin

# Register your models here.
from .models import Question
admin.site.register(Question)
```


 # Part 3: 모델과 관리자 페이지
> [Part 3: 모델과 관리자 페이지](https://docs.djangoproject.com/ko/3.0/intro/tutorial03/ "Part 2: 모델과 관리자 페이지")

# 뷰 추가하기
```python
# polls/views.py
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

# 뷰 urlpattern추가
```python
# polls/urls.py
from django.urls import path

from . import views

# namespace (여러개의 앱이 있을경우 app_name으로 구분함)
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

```

화면호출  
[http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)
```html
Mmmmmm...., What's up??
```

# 뷰 템블릿
```python
# polls/views.py
from django.template import loader
from django.http import HttpResponse
def index(request):   
    # Question._order.pub_date
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))  

or 
# import 및 사용방법이 간결해진다.
from django.shortcuts import render
def index(request):   
    # Question._order.pub_date
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)
```

```python
# mysite/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # mysite/temlates
            os.path.join(BASE_DIR, 'templates'),  
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```html
<!-- 
  templates/polls/index.html 
-->
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
