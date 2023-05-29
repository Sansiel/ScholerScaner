"""Модуль с моделью списка организаций"""

from django.db import models


class StudentModel:
    """Модель ученика"""

    id: int
    fullname: str
    dates: list

    def __init__(self, id: int, name: str):
        self.id = int(id)
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
    date: str
    theme: str

    def __init__(self, degree: str, day: str, month: str, theme: str, type_of_work: str = 'ответ на уроке',
                 date: str = '1/1/1999'):
        self.degree = degree
        self.day = day
        self.month = month
        self.theme = theme
        self.type_of_work = type_of_work
        self.date = date


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


class ProblemModel:
    text: str
    date: str
    theme: str
    type_of_work: str

    def __init__(self, date: str, theme: str, type_of_work: str, text: str = ''):
        self.date = date
        self.theme = theme
        self.type_of_work = type_of_work
        self.text = text


class StudentProblemsModel:
    fullname: str
    problems: list

    def __init__(self, name: str):
        self.fullname = name
