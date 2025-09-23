from django.contrib import admin
from .models.erpUser import *
from .models.model_group import *
from .models.teacher import *
from .models.student import *
admin.site.register([Student,Teacher,User,Table,TableType,GroupStudent,Parents,Course,Departments])


# Register your models here.
