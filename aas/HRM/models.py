from django.db import models
from django.db import models
from datetime import datetime , date, timedelta

import random

# Create your models here.

# Image name  change functions

def namechange(instance, filename):
        ext = filename.split('.')[-1]
        if instance.emp_id:
            return '{}/{}.{}'.format("image/Employees",instance.emp_id,'jpeg')
        else:
            pass

class Hradmin(models.Model):
    emp_id = models.CharField(max_length=50, default='', unique=True, primary_key=True)
    emp_name =  models.CharField(max_length=100, default='')
    emp_pass = models.CharField(max_length=200, default='')
    super_hr =  models.CharField(max_length=20, default='')

    def __str__(self):
        return self.emp_id

class Employee(models.Model):
    def password():
        return  str(random.randint(10000, 99999))

    emp_id =  models.CharField(max_length=50, default="", unique=True, primary_key=True)
    emp_name =  models.CharField(max_length=70, default="")
    emp_address =  models.CharField(max_length=150, default="")
    emp_email =  models.CharField(max_length=100, default="")
    emp_phone = models.CharField(max_length=30, default="")
    emp_dep = models.CharField(max_length=100, default="")
    emp_pass = models.CharField(max_length=500,default=password)
    emp_photo =  models.ImageField(upload_to=namechange, default="")

    def __str__(self):
        return self.emp_id

class Leave(models.Model):
    leave_id = models.CharField(max_length=50, default="", unique=True, primary_key=True)
    emp_id =  models.CharField(max_length=50, default="")
    emp_name =  models.CharField(max_length=70, default="")
    emp_dep = models.CharField(max_length=100, default="")
    s_date = models.DateField(default='')
    e_date = models.DateField(default='')
    l_day = models.IntegerField(default='')
    l_type = models.CharField(max_length=50, default='')
    l_status = models.CharField(max_length=50, default="")

    def __str__(self):
        name = self.leave_id+"(" +self.emp_id +")"
        return name

        
class Attendance(models.Model):
    def date():
        return date.today() - timedelta(days=1)
        

    def time():
        return datetime.now()
        

    emp_id = models.CharField(max_length=50, default = '', primary_key=True)
    emp_name = models.CharField(max_length=50, default = '' ,null= True, blank= True)
    attendace_date = models.DateField(default=date, null= True, blank= True)
    attendance_time = models.TimeField(default=time, null= True, blank= True)
    attendance_count = models.IntegerField(default = 0, blank=True, null=True)

    def __str__(self):
        value = self.emp_id 

        return value

class LeaveCount(models.Model):
    emp_id = models.CharField(max_length=50, default = '', primary_key=True)
    medical_leave = models.IntegerField(default=15, blank=True, null=True)
    personal_leave = models.IntegerField(default=30, blank=True, null=True)
    

    def __str__(self):
        value = self.emp_id 
        return value
