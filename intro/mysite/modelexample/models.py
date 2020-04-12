from django.db import models

# Create your models here.
class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'person'