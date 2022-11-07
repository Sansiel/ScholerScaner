"""Модуль работы с занятиями"""

from dataclasses import dataclass

from ScholerScaner.models.date import DateModel


@dataclass
class SubjectModel:
    """Модель занятия"""

    subject_id: int
    teachers_name: str
    date: DateModel
