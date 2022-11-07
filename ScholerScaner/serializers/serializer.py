""""""
from datetime import datetime
from typing import List

from ScholerScaner.models import BaseResponseModel


class BaseResponseSerializer:
    """Базовый класс для формирования ответа сервера из модели"""

    @staticmethod
    def to_representation(o: BaseResponseModel) -> dict:
        """Сериализация модели в словарь"""

        return {field: getattr(o, field) for field in o.get_fields()}

    @classmethod
    def to_multiple_representation(cls, instances: List[BaseResponseModel]):
        """Сериализация модели в список словарей"""

        return [cls.to_representation(instance) for instance in instances]


class BaseSerializer:
    """Base Serializer class"""

    def _format_date(self, date, parse_format='%d.%m.%y %H:%M:%S', format='%d.%m.%Y'):
        """
        Форматирование даты dd.mm.Y

        :param date: Дата
        :param parse_format: Исходный формат даты/времени
        :param format: Конечный формат даты/времени
        :return: Строка содержащая даты/время в конечном формате
        """
        if date is not None:
            datetime_object = datetime.strptime(date, parse_format)
            date = datetime_object.strftime(format)
        return date

    def to_representation(self, o):
        """

        :param o:
        :return:
        """
        raise NotImplementedError('Method to_representation is not implemented for %s.' % self.__class__.__name__)

    def to_internal_value(self, data):
        """

        :param data:
        :return:
        """
        raise NotImplementedError('Method to_internal_value is not implemented for %s.' % self.__class__.__name__)

    def to_multiple_representation(self, instances):
        """Сериализация модели в список словарей"""
        result = [self.to_representation(instance) for instance in instances]
        return result

    def to_multiple_internal_value(self, instances):
        """Сериализация из БД в список моделей"""

        result = [self.to_internal_value(instance) for instance in instances]
        return result
