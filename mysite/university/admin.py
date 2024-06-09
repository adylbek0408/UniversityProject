from django.contrib import admin
from .models import Faculty, Professor, Student, Courses, Cabinet, Schedule, RegistrationCourse, HomeWork, CheckHomeWork


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Professor)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'title', 'bio')
    search_fields = ('user__username', 'title', 'department__name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'enrollment_date', 'graduation_date')
    search_fields = ('user__username', 'department__name')


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department', 'professor')
    search_fields = ('name', 'code', 'department__name', 'professor__user__username')


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'building', 'capacity')
    search_fields = ('room_number', 'building')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'classroom', 'start_time', 'end_time', 'day_of_week')
    search_fields = ('course__name', 'classroom__room_number', 'day_of_week')


@admin.register(RegistrationCourse)
class RegistrationCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date_enrolled', 'grade')
    search_fields = ('student__user__username', 'course__name')


@admin.register(HomeWork)
class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'due_date')
    search_fields = ('course__name', 'title')


@admin.register(CheckHomeWork)
class CheckHomeWorkAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submission_date', 'grade')
    search_fields = ('assignment__title', 'student__user__username')
