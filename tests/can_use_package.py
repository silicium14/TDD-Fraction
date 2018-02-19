from unittest import TestCase


class CanUsePackage(TestCase):
    def test_can_add_fractions_from_package(self):
        """
        Special test that checks that we can use the installed version of the package
        """
        self.assertEqual(
            add(Fraction(7, 4), Fraction(4, 5)),
            Fraction(47, 15)
        )
