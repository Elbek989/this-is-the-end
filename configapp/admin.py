from django.contrib import admin
from .models.auth_user import *
from .models.model_group import *
from .models.auth_teacher import *
from .models.auth_student import *
admin.site.register([Student,Teacher,User,Table,TableType,GroupStudent,Parents,Course,Departments])


# Register your models here.
