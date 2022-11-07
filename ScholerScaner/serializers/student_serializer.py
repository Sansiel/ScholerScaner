"""Сериализатор создания товара в справочнике товаров"""
from ScholerScaner.models import StudentModel


class StudentSerializer:
    """ Сериализатор создания товара в справочнике"""

    def to_internal_value(self, data):
        """ Словарь в модель """
        student = StudentModel(
            fullname=data.get('fullname'),
            degree=data.get('degree'),

        )

        return student

    def to_representation(self, o: StudentModel):
        """ Модель в словарь """
        return {
            'fullname': o.fullname,
            'degree': o.degree,
        }
