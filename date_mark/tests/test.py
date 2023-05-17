from datetime import datetime
from django.test import TestCase
from date_mark.service import ImportService


class DateMarkTestCase(TestCase):

    def test_time(self):
        """time work"""
        for i in range (10):
            time = datetime.now()
            ImportService().get_recommend('9а')
            print(f" Start {i} scan. Time {datetime.now() - time}")
