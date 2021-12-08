from django.contrib import admin
from .models import Staff,Farm,Department,User
# Register your models here.
admin.site.register([Staff,Farm,Department,User])