from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from configapp.views.all_view  import (
    GroupStudentViewSet, TeacherViewSet, CourseViewSet,
    DepartmentsViewSet, TableViewSet, RoomsViewSet, TableTypeViewSet
)


from configapp.views import VerifyApi, RegisterApi, SendEmailAPI
from configapp.views.all_view import StudentApi, UserApi, TeacherAndUser, SendEmail

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Router — ModelViewSet uchun
router = DefaultRouter()
router.register('groups', GroupStudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('courses', CourseViewSet)
router.register('departments', DepartmentsViewSet)
router.register('tables', TableViewSet)
router.register('rooms', RoomsViewSet)
router.register('table-types', TableTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('student/', StudentApi.as_view()),
    path('students/<int:pk>/', StudentApi.as_view()),
    path('user/', UserApi.as_view()),
    path('teacher/', TeacherAndUser.as_view()),
    path('send_sms/', SendEmailAPI.as_view()),
    path('verify/', VerifyApi.as_view()),


    path('', include(router.urls)),
]
