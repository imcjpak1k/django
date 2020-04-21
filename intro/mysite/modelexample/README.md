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

> python manage.py migrate
# 필드

## Field Options

 - default
   - 기본값
   - 기본값은 value 또는 callable object
 - null 
   - False  : 기본값
   - True   : 저장시 빈값을 NULL로 저장
 - blank 
   - False  : 기본값
   - True   : 저장시 공백값을 허용
 - choices
   - tuple 또는 enumeration을 선택하여 사용함
   - 선언한 항목은 form widget의 select box로 표현됨

### Example
```python
# https://docs.djangoproject.com/ko/3.0/ref/models/fields/#field-choices
# choices tupule 1
class Person(models.Model):
    # selectbox 
    #  - value:S, text:Small
    #  - value:M, text:Medium
    #  - value:L, text:Large
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

# choices tupule 2
class Person(models.Model):
    # selectbox 
    #  - value:S, text:Small
    #  - value:M, text:Medium
    #  - value:L, text:Large
    #  - value:F, text:Free    (selectbox 기본선택됨)
    SMALL = 'S'
    MEDIUM  = 'M'
    LARGE = 'L'
    FREE = 'F'
    SHIRT_SIZES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (FREE, 'Free'),
    ]

    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=FREE)


# choices enumeration 1
class Person(models.Model):
    # selectbox 
    #  - value:Small, text:Small
    #  - value:Medium, text:Medium
    #  - value:Large, text:Large
    ShirtType = models.TextChoices('ShirtType', 'Small Medium Large')
    #  - value:1, text:Small
    #  - value:2, text:Medium
    #  - value:3, text:Large
    # ShirtType = models.IntegerChoices('ShirtType', 'Small Medium Large')

    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(blank=True, choices=ShirtType.choices, max_length=10)
    # shirt_size = models.IntegerField(blank=True, choices=ShirtType.choices)
    
# choices enumeration 2
class Person(models.Model):
    # selectbox 
    #  - value:S, text:Small
    #  - value:M, text:Medium
    #  - value:L, text:Large
    #  - value:F, text:Free
    class ShirtSize(models.TextChoices):
        SMALL = 'S', ('Small')
        MEDIUM  = 'M', ('Medium')
        LARGE = 'L', ('Large')
        FREE = 'F', ('Free')

    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=ShirtSize.choices, default=ShirtSize.FREE)
    
# choices enumeration 3
class Person(models.Model):
    # selectbox 
    #  - value:90, text:Small
    #  - value:100, text:Medium
    #  - value:105, text:Large
    #  - value:110, text:Free
    class ShirtSize(models.IntegerChoices):
        SMALL = 90, ('Small')
        MEDIUM  = 100, ('Medium')
        LARGE = 105, ('Large')
        FREE = 110, ('Free')

    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.IntegerField(choices=ShirtSize.choices, default=ShirtSize.FREE)
```


# 객체만들기
[creating-objects](https://docs.djangoproject.com/ko/3.0/ref/models/instances/#creating-objects, '오프젝트 만들기')     

# 쿼리만들기
[Create Query](https://docs.djangoproject.com/ko/3.0/topics/db/queries/, '쿼리만들기')
