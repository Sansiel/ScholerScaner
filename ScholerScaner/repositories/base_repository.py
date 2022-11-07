""" Модуль работы с базой данных """
import time

from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

from ScholerScaner.serializers.serializer import BaseResponseSerializer
from ScholerScaner.utils.utils import InfluxUtils


class BaseRepository:
    """Базовый репозиторий работы с базой данных"""

    utils = InfluxUtils

    def __init__(self, bucket: str = 'SchoolerBucket', organization: str = "Sindustry"):
        self.bucket = bucket
        self.organization = organization
        self.utils = self.utils()
        self.client = self.utils.client
        # self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.utils.switch_influx_database('test_influx')

    def save(self, measurements: list, tags: dict, fields: list):
        """Сохранение"""
        self.client.write_points(self.create_json_body(measurements, tags, fields))

    def create_json_body(self, measurements: list, tags: dict, fields: list):
        """Сохранение"""
        json_body = list()
        for measurement in measurements:
            json_body.append(
                {
                    "measurement": measurement,
                    "tags": tags,
                    "time": time.time(),
                    "fields": BaseResponseSerializer().to_multiple_representation(fields)
                }
            )
        return json_body

    # def create_tags_body(self, tags: list) -> list:
    #     """body tag"""
    #     json_body = list()
    #     for tag in tags:
    #         json_body.append(
    #             # self.deserialize(tag)
    #             tag
    #         )
    #     return json_body

    # def create_fields_body(self, fields: list) -> list:
    #     """body field"""
    #     json_body = list()
    #     for field in fields:
    #         json_body.append(
    #             # self.deserialize(field)
    #             BaseResponseSerializer().to_multiple_representation(fields)
    #         )
    #     return json_body

    def db_exec(self, sql: str):
        """ execution sql (for select)"""
        return self.client.query(sql)
