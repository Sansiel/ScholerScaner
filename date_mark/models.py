"""Модуль с моделью списка организаций"""

from django.db import models


class StudentModel(models.Model):
    """Модель ученика"""

    fullname: models.CharField(max_length=255)
    degree: models.CharField(max_length=2)


class ThemeModel(models.Model):
    """Модель тем"""

    name: models.CharField(max_length=255)


class DateModel(models.Model):
    """Модель организации для использования в списке"""

    day: models.CharField(max_length=2)
    month: models.CharField(max_length=2)
    year: models.CharField(max_length=4)
    merge_theme_id: models.ForeignKey(ThemeModel, on_delete=models.CASCADE)
    name: models.CharField(max_length=255)
    type_of_work: models.CharField(max_length=255)
    student: models.ForeignKey(StudentModel, on_delete=models.CASCADE)


class SubjectModel(models.Model):
    """Модель занятия"""

    teachers_name: models.CharField(max_length=255)
    date: models.ForeignKey(DateModel, on_delete=models.CASCADE)


class GradeModel(models.Model):
    """Модель класса"""

    name: models.CharField(max_length=255)
    subject: models.ForeignKey(SubjectModel, on_delete=models.CASCADE)