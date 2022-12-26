"""Модуль с моделью списка организаций"""

from django.db import models


class StudentModel:
    """Модель ученика"""

    fullname: str
    dates: list

    def __init__(self, name: str):
        self.fullname = name
        self.dates = []


class ThemeModel:
    """Модель тем"""

    name: str


class DateModel:
    """Модель организации для использования в списке"""

    day: str
    month: str
    year: str
    merge_theme_id: list
    degree: str
    type_of_work: str

    def __init__(self, degree: str, day: str, month: str):
        self.degree = degree
        self.day = day
        self.month = month


class SubjectModel:
    """Модель занятия"""

    teachers_name: str
    subject_name: str
    students: list

    def __init__(self, name: str):
        self.subject_name = name
        self.teachers_name = ''
        self.students = []


class GradeModel:
    """Модель класса"""

    name: str
    subjects: list

    def __init__(self, name: str, subjects: list):
        self.name = name
        self.subjects = subjects
