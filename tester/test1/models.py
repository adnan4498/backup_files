from django.db import models

# Create your models here.

class Student(models.Model):
    db_name = models.CharField(max_length=50)
    db_roll = models.IntegerField()
    db_city = models.CharField(max_length=50)



    def __str__(self):
        return str(self.db_name)


