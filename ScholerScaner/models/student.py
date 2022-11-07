"""Модуль работы с учениками"""

from dataclasses import dataclass

from ScholerScaner.models import BaseResponseModel


@dataclass
class StudentModel(BaseResponseModel):
    """Модель ученика"""

    # student_id: int
    fullname: str
    degree: str
