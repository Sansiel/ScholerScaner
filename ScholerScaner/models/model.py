"""Базовая модель для ответа от сервера"""

from dataclasses import dataclass


@dataclass
class BaseResponseModel:
    """Базовая модель для ответа от сервера"""

    def get_fields(self):
        """Получение полей модели"""

        return self.__dict__.keys()
