from rest_framework import serializers
from configapp.models.erpUser import User
from configapp.models.student import Student
from configapp.models.teacher import Teacher



class UserSerializer(serializers.ModelSerializer):
    # is_active=serializers.BooleanField(read_only=True)
    # is_teacher=serializers.BooleanField(read_only=True)
    # is_admin=serializers.BooleanField(read_only=True)
    # is_student=serializers.BooleanField(read_only=True)
    # is_staff=serializers.BooleanField(read_only=True)
    class Meta:
        model=User

        fields = ['phonenumber', 'password', 'email', 'is_staff','is_teacher', 'is_student', 'is_admin','is_active']
        read_only_fields = ['sms_kod','is_admin','is_staff']
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields = '__all__'
        read_only_fields=['user_id']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class TeacherPostSerializer(serializers.Serializer):
    teacher=TeacherSerializer()
    user=UserSerializer()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
class VerifySerializer(serializers.Serializer):
    email=serializers.EmailField()
    verify_kod=serializers.CharField()



