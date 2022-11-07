"""Модуль с моделью списка организаций"""

from dataclasses import dataclass

from ScholerScaner.models import StudentModel, ThemeModel


@dataclass
class DateModel:
    """Модель организации для использования в списке"""

    date_id: int
    day: str
    month: str
    merge_theme_id: ThemeModel
    name: str
    day: str
    month: str
    type_of_work: str
    student: StudentModel
