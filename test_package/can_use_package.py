from unittest import TestCase

import tdd_fractions


class CanUsePackage(TestCase):
    def test_can_add_fractions_from_package(self):
        """
        Special test that checks that we can use the installed version of the package
        RUN THIS TEST WIHTOUT THE LOCAL tdd_fractions MODULE IN THE PYTHON SEARCH PATH
        """
        self.assertEqual(
            tdd_fractions.add(tdd_fractions.Fraction(7, 4), tdd_fractions.Fraction(4, 5)),
            tdd_fractions.Fraction(51, 20)
        )
