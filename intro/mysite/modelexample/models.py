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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # shirt_size = models.CharField(max_length=1, choices=ShirtSize.choices, default=ShirtSize.FREE)
    # shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    # shirt_size = models.CharField(blank=True, choices=ShirtType.choices, max_length=10)
    shirt_size = models.IntegerField(choices=ShirtSize.choices, default=ShirtSize.FREE)

    def __str__(self):
        return f'{self.person_id}, {self.first_name}, {self.last_name}, {self.shirt_size} '

    class Meta:
        db_table = 'person'