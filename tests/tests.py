from unittest import TestCase

from tdd_fractions import add, Fraction, DenominatorIsZero


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

    def test_two_fifths_plus_two_equals_thriteen_fifths(self):
        self.assertEqual(
            add(Fraction(2, 5), 2),
            Fraction(12, 5)
        )


class FractionIsPrintedCorrecly(TestCase):
    def test_fraction_representation(self):
        self.assertEqual(
            "15/8",
            str(Fraction(15, 8))
        )


class AddTwoFractions(TestCase):
    def test_one_fifth_plus_one_sixth_equals_eleven_on_thirty(self):
        self.assertEqual(
            Fraction(11, 30),
            add(Fraction(1, 5), Fraction(1, 6))
        )


class FractionReduction(TestCase):
    def test_one_fourth_plus_one_fourth_equals_one_half(self):
        self.assertEqual(
            Fraction(1, 2),
            add(Fraction(1, 4), Fraction(1, 4))
        )


class FractionInstanciationConstraints(TestCase):
    def test_cannot_create_a_fraction_with_denominator_zero(self):
        with self.assertRaises(DenominatorIsZero):
            _ = Fraction(8, 0)
