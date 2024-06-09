from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


def __str__(self):
    return self.name


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Courses(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField()
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Cabinet(models.Model):
    room_number = models.CharField(max_length=10)
    building = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.building} {self.room_number}"


class Schedule(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ])

    def __str__(self):
        return f"{self.course} in {self.classroom} on {self.day_of_week} from {self.start_time} to {self.end_time}"


class RegistrationCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    grade = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.course}"


class HomeWork(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.course}"


class CheckHomeWork(models.Model):
    assignment = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateField()
    grade = models.CharField(max_length=2, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.assignment}"
