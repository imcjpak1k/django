[모델](https://docs.djangoproject.com/ko/3.0/topics/db/models/, '모델')
# 앱생성 
> python manage.py startapp modelexample

# 앱등록
```python
# mysite/settings.py
# Application definition
INSTALLED_APPS = [
    'modelexample.apps.ModelexampleConfig',
    ...
]
```

# Person 모델생성 
아래와 같이 Person테이블을 생성하도록 하며, 컬럼은 2개만 정의되어 하도록 한다.  

```python
# modelexample/models.py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

# migration 
> python manage.py makemigrations modelexample  
> python manage.py sqlmigrate modelexample 0001 
```sql
BEGIN;
--
-- Create model Person  
--  
CREATE TABLE "modelexample_person" (    
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,    
    "first_name" varchar(30) NOT NULL,  
    "last_name" varchar(30) NOT NULL
    );
COMMIT;
```   
변경내용(DDL)을 보면 정의하지 않는 내용 또는 다른 내용을 확인할 수 있다.
1. **테이블명(모델명)이 다르다.**   
   - django의 테이블명은 다음의 형태로 생성된다.
   - _*{app name}_{class name}*_
   - 테이블명을 수동으로 정의하고 한다면 **Model Meta Options**으로 해결
   ```python
    # modelexample/models.py
    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

        class Meta:
            db_table = 'person'
   ```
   > python manage.py makemigrations modelexample   
   > python manage.py sqlmigrate modelexample 0006
   ```sql
    > python manage.py makemigrations modelexample
    Migrations for 'modelexample':
    modelexample\migrations\0005_auto_20200411_2141.py
        - Rename table for person to (default)

    > python manage.py sqlmigrate modelexample 0006
    BEGIN;
    --
    -- Rename table for person to person
    --
    ALTER TABLE "modelexample_person" RENAME TO "person";
    COMMIT;
   ```
2. **정의하지 않은 컬럼(id)가 추가되어 있다.** 
   - 모델의 primarykey가 정의되어 있지 않으면 자동으로 생성한다고 한다.
   - id컬럼 즉 primary key를 사용자가 정의한다면 자동생성은 되지 않는다.
   ```python
    # modelexample/models.py
    class Person(models.Model):
        person_id = models.AutoField(primary_key=True)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

        class Meta:
            db_table = 'person'
   ```
   ```sql
    > python manage.py makemigrations modelexample
    Migrations for 'modelexample':
    modelexample\migrations\0001_initial.py
        - Create model Person

    > python manage.py sqlmigrate modelexample 0001
    BEGIN;
    --
    -- Create model Person
    --
    CREATE TABLE "person" ( 
        "person_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
        "first_name" varchar(30) NOT NULL, 
        "last_name" varchar(30) NOT NULL
        );
    COMMIT;
   ```


