from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from configapp.models.erpUser import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from configapp.models import *
from configapp.serializers.userserilizers import *


class UserApi(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['DELETE'])
    def remove_user(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        user = self.get_object()
        user.remove(user_id)
        user.save()
        serializer = UserSerializer()
        return Response(data=serializer.data)

class StudentApi(APIView):

    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=StudentSerializer)
    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=StudentSerializer)
    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response({"detail": "Deleted"}, status=status.HTTP_204_NO_CONTENT)


