from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class Farm (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    no_produce = models.CharField(blank=True, max_length=100)
    produce_categories = models.CharField (blank=True, max_length=100)
    location = models.TextField(blank=True, max_length=700)
    about = models.TextField(blank=True, max_length=2000)

    def __str__(self):
        return self.name;
    

class Department (models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=700, default='Description goes here')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("farm:dept_single", kwargs={"pk": self.pk})
    

class Staff (models.Model):

    image = models.ImageField(blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    stipend = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10)
    country = models.CharField(max_length=20, default='Ghana')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    work_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name+'-'+self.last_name

    def get_absolute_url(self):
        return reverse("farm:staff_single", kwargs={"pk": self.pk})
    
    

class User (AbstractUser):
    image = models.ImageField(blank=True)


class Produce (models.Model):
    name = models.CharField(max_length=50)
    types = models.CharField(max_length=50)
    total = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class TimeLine(models.Model):
    number = models.IntegerField()
    farm = models.CharField(max_length=2)
    others = models.TextField(max_length=9000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Sales (models.Model):
    types = models.CharField(max_length=12)
    customer = models.CharField(max_length=180,default='Anonymous')
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.types

class Debtors (models.Model):
    name = models.CharField(max_length=90)
    file_no = models.CharField(max_length=50)
    quantity = models.IntegerField()
    department = models.CharField(max_length=50)
    amount = models.IntegerField()
    signature = models.ImageField()
    created = models.DateField(auto_now_add=True, null=True)


class Activities (models.Model):
    

    date = models.DateField()
    
    activity1 = models.CharField(max_length=100,blank=False)
    activity2 = models.CharField(max_length=100,blank=True)
    activity3 = models.CharField(max_length=100,blank=True)
    activity4 = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return "Activities on "+self.date


class Expenses (models.Model):
    date = models.DateField()
    activity = models.CharField(max_length=100)
    investment = models.PositiveIntegerField()

    def __str__(self):
        return "Expenses for "+self.date
