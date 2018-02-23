from unittest import TestCase

from tdd_fractions import add


class AddIntegers(TestCase):
    def test_zero_plus_zero_equals_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_one_plus_zero_equals_one(self):
        self.assertEqual(add(0, 1), 1)

