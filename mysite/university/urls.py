from django.urls import path
from .views import *

urlpatterns = [
    path('faculty/', FacultyViewSet.as_view({'get': 'list', 'post': 'create'}), name='faculty-list'),
    path('faculty/<int:pk>/', FacultyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='faculty-detail'),
    path('professor/', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}), name='professor-list'),
    path('professor/<int:pk>/', ProfessorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='professor-detail'),
    path('student/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('student/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='student-detail'),
    path('course/', CoursesViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    path('course/<int:pk>/', CoursesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='course-detail'),
    path('cabinet/', CabinetViewSet.as_view({'get': 'list', 'post': 'create'}), name='cabinet-list'),
    path('cabinet/<int:pk>/', CabinetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='cabinet-detail'),
    path('schedule/', ScheduleViewSet.as_view({'get': 'list', 'post': 'create'}), name='schedule-list'),
    path('schedule/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='schedule-detail'),
    path('registration_course/', RegistrationCourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='registration_course-list'),
    path('registration_course/<int:pk>/', RegistrationCourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='registration_course-detail'),
    path('home_work/', HomeWorkViewSet.as_view({'get': 'list', 'post': 'create'}), name='home_work-list'),
    path('home_work/<int:pk>/', HomeWorkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='home_work-detail'),
    path('check_home_work/', CheckHomeWorkViewSet.as_view({'get': 'list', 'post': 'create'}), name='check_home_work-list'),
    path('check_home_work/<int:pk>/', CheckHomeWorkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='check_home_work-detail'),
]

