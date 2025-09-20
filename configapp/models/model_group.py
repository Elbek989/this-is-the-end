from .student import *
from .erpUser import *
from .teacher import *
class Day(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500,blank=True,null=True)

    def str(self):
        return self.title

class Rooms(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500,blank=True,null=True)

    def str(self):
        return self.title

class TableType(BaseModel):
    title = models.CharField()
    descriptions = models.CharField(max_length=500,blank=True,null=True)

    def str(self):
        return self.title

class Table(BaseModel):
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey(Rooms,on_delete=models.RESTRICT)
    type = models.ForeignKey(TableType,on_delete=models.RESTRICT)
    descriptions = models.TextField(blank=True,null=True)

    def str(self):
        return self.start_time.str() + " " + self.end_time.str()

class GroupStudent(BaseModel):
    title = models.CharField()
    course = models.ForeignKey(Course,on_delete=models.RESTRICT,related_name='course')
    teacher = models.ManyToManyField(Teacher,related_name='get_teacher')
    table = models.ForeignKey(Table,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_time = models.DateField()
    descriptions = models.CharField(blank=True,null=True)

    def str(self):
        return self.title