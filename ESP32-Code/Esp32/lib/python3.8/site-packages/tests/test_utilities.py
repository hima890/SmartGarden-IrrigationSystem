import unittest
from esp.utilities import underscore_to_titlecase, titlecase_to_underscore


class TestUtilities(unittest.TestCase):

    def test_can_convert_to_titlecase(self):
        self.assertEqual(underscore_to_titlecase('test_foo'), 'TestFoo')

    def test_can_convert_to_underscore(self):
        self.assertEqual(titlecase_to_underscore('TestFoo'), 'test_foo')
