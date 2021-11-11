import unittest
from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Help_Site.settings')
import django
django.setup()
from Application.models import Thread, Post


class MyTestCase(unittest.TestCase):
    #def setUp(self):



    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
