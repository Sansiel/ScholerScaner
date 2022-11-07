"""Модуль работы с темами занятий"""

from dataclasses import dataclass


@dataclass
class ThemeModel:
    """Модель тем"""

    theme_id: int
    name: str
