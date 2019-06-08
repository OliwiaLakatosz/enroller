from django.test import TestCase

class TestTestCase(TestCase):
    def setUp(self):
        print("SetUp")

    def test_that_pass(self):
        print("This test just pass")