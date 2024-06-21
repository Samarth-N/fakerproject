from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.Charfield(max_length=30)
    roll=models.IntegerField()
    marks=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()
    
 
