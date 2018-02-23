from unittest import TestCase

from tdd_fractions import add


class Simplest(TestCase):
    def test_zero_plus_zero_equals_zero(self):
        self.assertEqual(add(0, 0), 0)
