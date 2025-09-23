from symtable import Class

from rest_framework import serializers

from configapp.models import GroupStudent, Table, Rooms, TableType
from configapp.models.erpUser import User
from configapp.models.student import Student
from configapp.models.teacher import Teacher, Departments, Course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phonenumber', 'password', 'email', 'is_staff','is_teacher', 'is_student', 'is_admin','is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields = '__all__'
        read_only_fields=['user_id']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        reaf_only_field=['user']

class TeacherPostSerializer(serializers.Serializer):
    teacher=TeacherSerializer()
    user=UserSerializer()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
class VerifySerializer(serializers.Serializer):
    email=serializers.EmailField()
    verify_kod=serializers.CharField()

class DepartmenstSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields='__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=GroupStudent
        fields='__all__'
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields='__all__'
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rooms
        fields='__all__'
class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TableType
        fields = '__all__'


class StudentAndUserSerializer(serializers.Serializer):
    user = UserSerializer()
    student = StudentSerializer()

