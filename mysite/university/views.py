from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user__username', 'department']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['user__username']


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['professor', 'name']
    search_fields = ['name']


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class RegistrationCourseViewSet(viewsets.ModelViewSet):
    queryset = RegistrationCourse.objects.all()
    serializer_class = RegistrationCourseSerializer


class HomeWorkViewSet(viewsets.ModelViewSet):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer


class CheckHomeWorkViewSet(viewsets.ModelViewSet):
    queryset = CheckHomeWork.objects.all()
    serializer_class = CheckHomeWorkSerializer

