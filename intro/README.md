# example : django intro
# Part 1: 요청과 응답
> [튜토리얼: Part 1: 요청과 응답](https://docs.djangoproject.com/ko/3.0/intro/tutorial01/ "튜토리얼: Part 1: 요청과 응답 ")

## 프로젝생성
> django-admin startproject mysite

## 앱생성
> cd mysite 
> python manage.py startapp polls

## polls/views.py view추가
```python
# polls/views.py
from django.http import request   
from django.http import HttpResponse  

# Create your views here.
def index(request):   
    return HttpResponse("Hello wrold. You're at the polls index.")    
```


## polls/urls.py 생성
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

## DATABASE
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
## TIME_ZONE
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

## 데이터베이스 및 테이블생성 
> python manage.py migrate

## 모델만들기
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

## 모델활성화
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
## makemigrations
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

## mirgrate
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

## 대화식 python shell
> python manage.py shell

## 관리자생성
> python manage.py createsuperuser
> 

```bash
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


# Part 3: 뷰와 템플릿
> [Part 3: 뷰와 템플릿](https://docs.djangoproject.com/ko/3.0/intro/tutorial03/ "Part 3: 뷰와 템플릿")

## 뷰 추가하기
```python
# polls/views.py

def index(request):   
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)  

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```


## urlpattern추가
```python
# polls/urls.py
from django.urls import path

from . import views

# namespace (여러개의 앱이 있을경우 app_name으로 구분함)
# app_name = 'polls'

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

[http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)
```html
Mmmmmm...., What's up??
```

## template, loader, lender
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
  mysite/mysite/
  mysite/polls/
  mysite/templates/polls/index.html 
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

## 템플릿 시스템 사용하기
- question_id로 데이터를 조회
- polls/detail.html 템블릿 이동
- 조회 결과값(dict)은 render함수에 request와 같이 전달한다.
```python
# polls/views.py
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})
```
- dict형태로 전달받아 template에 출력
- question변수에 question model객체를 가져다 출력한다.
- question.choice_set함수은 질문의 답변목록을 가져오는 역할을 하는 것으로, model에서 ForeignKey를 설정하면 생성되는 함수인듯 함....
- (question의 pk로 choice데이터를 조회 후 반환)

```html
<!-- templates/polls/detail.html -->
<ul>
<!-- 질문내용 -->
<h1>{{ question.question_text }}</h1>
<!-- 답변내용 -->
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

## 템플릿에서 하드코딩된 URL 제거하기
polls/urls.py 파일에 정의되어 있는 'detail'의 url 정보를 가져다 출력하므로 url정보를 변경하고자 하는 경우에는 urls.py의 path정보만 수정한다.
```html
<!-- 
  templates/polls/index.html 
-->
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <!-- 
            path('<int:question_id>/', views.detail, name='detail'),
         -->
        <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
        
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

## url namespace(app_name)
- namespace(app_name)설정은 여러 app이 있을때 충돌을 방지해주는 역할을 하며, 설정은 아래와 같이 진행한다.
- 해당 url을 사용하는 화면(html)이 있으면 url에 namespace를 추가 입력하도록 한다.
- 즉, namespace를 추가 및 수정하게 된다면 노가다를 해야한다는 이야기이므로 namespace는 신중한게 입력하도록 하자.

```python
# polls/urls.py

# namespace
app_name = 'polls'
```

```html
<!-- 
  templates/polls/index.html 
-->
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
    <!--
        namespace추가
        'detail' ==>> 'polls:detail'
    -->
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
        
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```




# Part 4: 폼과 기본 뷰
> [Part 4: 폼과 기본 뷰](https://docs.djangoproject.com/ko/3.0/intro/tutorial04/ "Part 4: 폼과 기본 뷰")
## form submit
기존의 detail.html파일에서 투표기능 추가
- 에러메세지 출력 추가
- csrf_token : 중복투표방지 token생성
- forloop.counter : for문의 반복횟수 표시
- submit 추가
```html
<!-- polls/templates/polls/detail.html -->
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```

question_id의 선택값(투표) 기능추가
- question_id로 Question조회
- Question의 Choice값 가져오기
- 단, 선택값이 존재하지 않는 경우에는 오류메세지 전송
- exception이 발생하지 않으면 else구문을 정상적으로 수행
- 저장 후 페이지 이동

> reverse : URLconf(urls.py)의 path정보로 URL반환   
> HttpResponseRedirect : url로 페이지이동   
> [request, response 정보](https://docs.djangoproject.com/ko/3.0/ref/request-response/, 'https://docs.djangoproject.com/ko/3.0/ref/request-response/')


```python
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

def vote(request, question_id):
    # question_id로 Question조회
    question = get_object_or_404(Question, pk=question_id)

    try:
        # question객체에서 choice값 가져오기(fk)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # 투표 횟수 증가 및 저장
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing with POST data. 
        # This prevents data from being posted twice if a user hits the Back button.
        # EX) reverse('polls:results', args=(1,)) 
        # '/polls/1/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

```python
from django.shortcuts import get_object_or_404, render

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

```html
<!-- polls/templates/polls/result.html -->
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```
 
위 소스에는 문제점이 있다고 한다.
투표시 동시에 접근한 경우 투표 카운트가 정상적으로 수행하지 못할수가 있다.
여러 클라이언트가 동시에 접속해서 동일한 값을 조회 후 저장하는 경우에
정상적인 결과값을 db에 반영 못할수 가 있다는 것이다.    

> ex)     
> 홍길동 조회시 투표횟수 22회   -> 저장 -> 23회   
> 강감찬 조회시 투표횟수 22회   -> 저장 -> 23회   
> 
> 정상적이라면 다음과 같이 되어야 한다.   
> 
> 홍길동 조회시 투표횟수 22회   -> 저장 -> 23회   
> 강감찬 조회시 투표횟수 22회   -> 저장 -> 24회   

이 문제를 해결할 수 있는 방법을 알아보려면 [Avoiding race conditions using F()](https://docs.djangoproject.com/ko/3.0/ref/models/expressions/#avoiding-race-conditions-using-f, "Avoiding race conditions using F()") 를 참고하세요

## 제네릭 뷰 사용하기

 # Part 5: 테스팅
> [Part 5: 테스팅](https://docs.djangoproject.com/ko/3.0/intro/tutorial05/ "Part 5: 테스팅")


 # Part 6: 정적 파일
> [Part 6: 정적 파일](https://docs.djangoproject.com/ko/3.0/intro/tutorial06/ "Part 6: 정적 파일")

 # Part 7: 관리자 페이지 커스터마이징
> [Part 7: 관리자 페이지 커스터마이징](https://docs.djangoproject.com/ko/3.0/intro/tutorial07/ "Part 7: 관리자 페이지 커스터마이징")

