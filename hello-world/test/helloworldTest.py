import unittest
from app.helloworld import *

class HelloWorldTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_hello_world(self):
        self.assertEqual(hello_world()["message"], "success");