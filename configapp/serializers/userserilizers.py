from rest_framework import serializers
from configapp.models.erpUser import User
from configapp.models.student import Student
from configapp.models.teacher import Teacher



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


