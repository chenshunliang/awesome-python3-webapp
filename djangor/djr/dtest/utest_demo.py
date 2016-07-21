import unittest
from django.test import TestCase, Client


class DTest(TestCase):
    def test_int(self):
        self.assertEqual(9 / 3, 3)

        # def test_baidu(self):
        #     res = self.client.get('http://www.baidu.com')
        #     self.assertEqual(res.status_code, 200)
