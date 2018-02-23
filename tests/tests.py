from unittest import TestCase

from tdd_fractions import add, Fraction


class AddIntegers(TestCase):
    def test_zero_plus_zero_equals_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_one_plus_zero_equals_one(self):
        self.assertEqual(add(0, 1), 1)


class Equality(TestCase):
    def test_same_fractions_are_equal(self):
        self.assertEqual(
            Fraction(1, 2),
            Fraction(1, 2)
        )

    def test_different_fractions_are_not_equal(self):
        self.assertNotEqual(
            Fraction(3, 2),
            Fraction(4, 5)
        )


class AddFractionAndInteger(TestCase):
    def test_one_plus_one_half_equals_two_halves(self):
        self.assertEqual(
            add(1, Fraction(1, 2)),
            Fraction(3, 2)
        )
