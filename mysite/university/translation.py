from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Professor)
class ProfessorTranslationOptions(TranslationOptions):
    fields = ('title', 'bio')


@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    pass


@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Cabinet)
class CabinetTranslationOptions(TranslationOptions):
    fields = ('room_number', 'building')


@register(RegistrationCourse)
class RegistrationCourseTranslationOptions(TranslationOptions):
    fields = ('grade',)


@register(HomeWork)
class HomeWorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CheckHomeWork)
class HomeWorkTranslationOptions(TranslationOptions):
    fields = ('grade', 'feedback')
