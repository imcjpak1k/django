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
 - help_text
   - form wedget에 표현됨. 
   - 몰라도 됨
 - primary_key
   - False  : 기본값
   - True   : Field를 primary key로 사용함. 
 - unique
   - False  : 기본값
   - True   : unique Field
 - Verbose field name
   - 생략가능하며, 위치인자로 입력하며, 해당 내용은 form widget에 표현됨.
   - admin화면에서 해당 필드명으로 표현됨 (몰라도 됨)
 - db_column
   - 데이터베이스의 컬럼이름을 지정하며, 미 지정시 필드이름을 사용한다.
 - db_index
   - False  : 기본값
   - True   : 필드의 인덱스 생성
 - db_tablespace
   - ....
 - editable
   - ....
 - error_messages
   - ....
 - unique
   - ....
 - unique_for_date
   - ....
 - unique_for_month
   - ....
 - unique_for_year
 - validators
### Example
```python
# https://docs.djangoproject.com/ko/3.0/ref/models/fields/#field-choices
# choices tupule 1
from django.db import models
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

# Verbose filed name
    first_name = models.CharField('첫번째 이름', max_length=30)
```
## Field types
- AutoField
  - 자동증가하는 IntegerField를 생성 함.
- BigAutoField
  - 1부터 9223372036854775807까지의 숫자를 입력할 수 있는 필드생성.
- BinaryField
- BooleanField
- CharField
- DateField
- DateTimeField
- DecimalField
- DurationField
- EmailField
- FileField
- FilePathField   
- FloatField
- ImageField
- IntegerField
- GenericIPAddressField
- NullBooleanField
- PositiveIntegerField
- PositiveSmallIntegerField
- SlugField
- SmallAutoField
- SmallIntegerField
- TextField
- TimeField
- URLField
- UUIDField
## relationships field
### ForeignKey
Many-to-one relationships은 2개의 위치인자가 필요하다.
 - 모델과 관련된 클래스 이름
 - on_delete option

### Many-to-one relationships Example
```python
from django.db import models

class Manufacturer(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
```
```sql
BEGIN;
--
-- Create model Manufacturer
--
CREATE TABLE "modelexample_manufacturer" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT
);
--
-- Create model Car
--
CREATE TABLE "modelexample_car" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "manufacturer_id" integer NOT NULL REFERENCES "modelexample_manufacturer" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "modelexample_car_manufacturer_id_b7baabb5" ON "modelexample_car" ("manufacturer_id");
COMMIT;
```

### Many-to-Many relationships Example
ManyToManyField를 정의할때에는 2개의 모델 중 하나의 모델에만 정의하여야 한다.
```python
class Topping(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
```
```sql
BEGIN;
--
-- Create model Topping
--
CREATE TABLE "modelexample_topping" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT
);
--
-- Create model Pizza
--
CREATE TABLE "modelexample_pizza" ( 
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT
);
CREATE TABLE "modelexample_pizza_toppings" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "pizza_id" integer NOT NULL REFERENCES "modelexample_pizza" ("id") DEFERRABLE INITIALLY DEFERRED, 
    "topping_id" integer NOT NULL REFERENCES "modelexample_topping" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE UNIQUE INDEX "modelexample_pizza_toppings_pizza_id_topping_id_e07eee72_uniq" ON "modelexample_pizza_toppings" ("pizza_id", "topping_id");
CREATE INDEX "modelexample_pizza_toppings_pizza_id_785cde20" ON "modelexample_pizza_toppings" ("pizza_id");
CREATE INDEX "modelexample_pizza_toppings_topping_id_a71eb4fa" ON "modelexample_pizza_toppings" ("topping_id");
COMMIT;
```

다른방법으로는 M:M모델을 정의하여 해결한다.

```python
class Topping(models.Model):
    pass

class Pizza(models.Model):
    pass

class MakePizza(models.Model):
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
```

```sql
--
-- Create model Topping
--
CREATE TABLE "modelexample_topping" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT
);
--
-- Create model Pizza
--
CREATE TABLE "modelexample_pizza" ( 
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT
);
--
-- Create model MakePizza
--
CREATE TABLE "modelexample_makepizza" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "pizza_id" integer NOT NULL REFERENCES "modelexample_pizza" ("id") DEFERRABLE INITIALLY DEFERRED, 
    "topping_id" integer NOT NULL REFERENCES "modelexample_topping" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX "modelexample_makepizza_pizza_id_99256ae0" ON "modelexample_makepizza" ("pizza_id");
CREATE INDEX "modelexample_makepizza_topping_id_f06b8dfa" ON "modelexample_makepizza" ("topping_id");
COMMIT;
```
## Model meta option
- abstract
  - False   : 기본값
  - True    : 추상클래스 선언
- app_label
- base_manager_name
- db_table
  - 모델에서 사용할 데이테베이스 테이블이름
- db_tablespace
- default_manager_name
- default_related_name
- get_latest_by
- managed
- order_with_respect_to
- ordering
- permissions
- default_permissions
- proxy
- required_db_features
- required_db_vendor
- select_on_save
- indexes
- unique_together
- index_together
- constraints
- verbose_name
- verbose_name_plural
- 
# 객체만들기
[creating-objects](https://docs.djangoproject.com/ko/3.0/ref/models/instances/#creating-objects, '오프젝트 만들기') 
모델을 생성할 때 다음과 같은 방법으로 class를 만들어서 진행하였다. 
```python
# models.py
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
```

```shell
C:\Users\imcjp\workspace\vscode\django\intro\mysite>python manage.py makemigrations modelexample  
C:\Users\imcjp\workspace\vscode\django\intro\mysite>python manage.py migrate modelexample  

C:\Users\imcjp\workspace\vscode\django\intro\mysite>python manage.py shell
>>> from modelexample.models import Book
>>> book = Book(title='테스트입력00001')
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
```

## classmethod 추가
```python
# models.py
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    @classmethod
    def create(cls, title):
        book = cls(title=title)
        # do something with the book
        return book
```

```shell
C:\Users\imcjp\workspace\vscode\django\intro\mysite>python manage.py shell
>>> from modelexample.models import Book 
>>> book = Book.create('테슽스입력00002')
>>> book
<Book: 테슽스입력00002>
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: 테스트입력00001>, <Book: 테슽스입력00002>]>
```

## custom manager(일반적인방법)
```python
# models.py
from django.db import models
class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book

class Book(models.Model):
    title = models.CharField(max_length=100)
    objects = BookManager()

    def __str__(self):
        return self.title
```

```shell
C:\Users\imcjp\workspace\vscode\django\intro\mysite>python manage.py shell
>>> from modelexample.models import Book 
>>> book = Book.objects.create_book('manager test') 
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: 테스트입력00001>, <Book: 테슽스입력00002>, <Book: manager test>]>
```

# 쿼리만들기
## ㅇㅇ