from django.db import models

# Create your models here.
class Person(models.Model):
    # enumeration
    # ShirtType = models.TextChoices('ShirtType', 'Small Medium Large')
    # SMALL = 'S'
    # MEDIUM  = 'M'
    # LARGE = 'L'
    # FREE = 'F'
    # SHIRT_SIZES = [
    #     (SMALL, 'Small'),
    #     (MEDIUM, 'Medium'),
    #     (LARGE, 'Large'),
    #     (FREE, 'Free'),
    # ]
    
    # class ShirtSize(models.TextChoices):
    #     SMALL = 'S', ('Small')
    #     MEDIUM  = 'M', ('Medium')
    #     LARGE = 'L', ('Large')
    #     FREE = 'F', ('Free')
    class ShirtSize(models.IntegerChoices):
        SMALL = 90, ('Small')
        MEDIUM  = 100, ('Medium')
        LARGE = 105, ('Large')
        FREE = 110, ('Free')


    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, help_text='성')
    last_name = models.CharField('test입력', max_length=30, help_text='이름')
    # shirt_size = models.CharField(max_length=1, choices=ShirtSize.choices, default=ShirtSize.FREE)
    # shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    # shirt_size = models.CharField(blank=True, choices=ShirtType.choices, max_length=10)
    shirt_size = models.IntegerField(choices=ShirtSize.choices, default=ShirtSize.FREE)

    def __str__(self):
        return f'{self.person_id}, {self.first_name}, {self.last_name}, {self.shirt_size} '

    class Meta:
        db_table = 'person'


class Manufacturer(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)



class Topping(models.Model):
    pass

class Pizza(models.Model):
    # toppings = models.ManyToManyField(Topping)
    pass

class MakePizza(models.Model):
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)