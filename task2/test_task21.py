from unittest import TestCase

from task21 import is_leap


class TestTask(TestCase):

    def setUp(self):
        """Init"""

    def test_is_leap(self):
        self.assertFalse(is_leap(1990))
        self.assertTrue(is_leap(2020))

    def tearDown(self):
        """Finish"""

