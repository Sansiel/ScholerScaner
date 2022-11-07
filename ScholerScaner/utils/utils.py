from django.conf import settings

from influxdb import InfluxDBClient
# import influxdb_client
import os
# from influxdb_client import InfluxDBClient, Point, WritePrecision
# from influxdb_client.client.write_api import SYNCHRONOUS

import logging

logger = logging.getLogger(__name__)


class InfluxUtils:
    """Утилиты Influx"""


    example_token = 'ddMZE4c-MoLJCDQp_p1SJkgHPXqRzFZ25szVXOM0jREsMr12NgeLHhX7IW8A1aedrRSBJR8b1Z-xnIC-vp7N-g=='

    def __init__(self):
        self.influx_token = os.environ.get("INFLUXDB_TOKEN", self.example_token)
        self.org = "Sindustry"
        self.host = "http://localhost"
        self.username = 'Sansiel'
        self.password = 'password'

        # client = influxdb_client.InfluxDBClient(url=url, token=influx_token, org=org)
        self.client = InfluxDBClient(
            host=self.host,
            port=8086,
            username=self.username,
            password=self.password,
            ssl=True,
            verify_ssl=True
        )

    def create_influx_database(self, name: str = 'pyexample'):
        """Create database"""
        self.client.create_database(name)
        self.client.switch_database(name)
        return self.client

    def switch_influx_database(self, name: str = 'pyexample'):
        """Switch database"""
        list_db = self.client.get_list_database()
        for db in list_db:
            if db['name'] == name:
                self.client.switch_database(name)
                return self.client
        return self.create_influx_database(name)
