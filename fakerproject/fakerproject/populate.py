import os
import django
#run administrative task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakerproject.settings')
django.setup()
from faker import Faker
from myApp.models import Student
f=Faker()
def Generate_data(n):
    for i in range(n):
        fname=f.name()
        froll=f.random_int(min=1,max=100)
        fmarks=f.random_int(min=1,max=100)
        fdob=f.date_of_birth()
        femail=f.email()
        s=Student.objects.get_or_create(name=fname,roll=froll,marks=fmarks,dob=fdob,email=femail)
Generate_data(20)