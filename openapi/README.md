
# venv
> python -m venv venv

# requirements
> pip install -r requirements/local.txt

# 프로젝생성
> django-admin startproject {프로젝트명}

# 앱생성
> django-admin startapp {앱이름}
> 

# 서버실행
> manage.py runserver 5500

# 서버실행(local_settings.py를 사용하도록 변경)
> python manage.py runserver 8888 --settings=openapi.settings.local