# serializers.py
from rest_framework import serializers
from .models import Faculty, Professor, Student, Courses, Cabinet, Schedule, RegistrationCourse, HomeWork, CheckHomeWork


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display the user as a string
    department = serializers.StringRelatedField()

    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    department = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    professor = serializers.StringRelatedField()

    class Meta:
        model = Courses
        fields = '__all__'


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    classroom = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = '__all__'


class RegistrationCourseSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()

    class Meta:
        model = RegistrationCourse
        fields = '__all__'


class HomeWorkSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()

    class Meta:
        model = HomeWork
        fields = '__all__'


class CheckHomeWorkSerializer(serializers.ModelSerializer):
    assignment = serializers.StringRelatedField()
    student = serializers.StringRelatedField()

    class Meta:
        model = CheckHomeWork
        fields = '__all__'
