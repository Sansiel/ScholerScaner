"""Модуль работы с классами учеников"""

from dataclasses import dataclass

from ScholerScaner.models import SubjectModel


@dataclass
class GradeModel:
    """Модель класса"""

    grade_id: int
    name: str
    subject: SubjectModel
