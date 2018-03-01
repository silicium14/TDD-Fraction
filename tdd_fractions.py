from typing import Union

import math


class Fraction(object):
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise DenominatorIsZero()
        numerator, denominator = self._move_sign_on_numerator(numerator, denominator)
        numerator, denominator = self._simplify(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return (self.numerator == other.numerator
                and self.denominator == other.denominator)

    def __repr__(self):
        return "{numerator}/{denominator}".format(
            numerator=self.numerator, denominator=self.denominator
        )

    @staticmethod
    def _move_sign_on_numerator(numerator: int, denominator: int):
        if math.copysign(1, denominator) < 0:
            numerator = - numerator
            denominator = abs(denominator)
        return numerator, denominator

    @staticmethod
    def _simplify(numerator: int, denominator: int):
        greatest_common_divisor = math.gcd(numerator, denominator)
        return int(numerator/greatest_common_divisor), int(denominator/greatest_common_divisor)


def _simplify_fraction(fraction: Fraction):
    greatest_common_divisor = math.gcd(fraction.numerator, fraction.denominator)
    return Fraction(
        int(fraction.numerator/greatest_common_divisor),
        int(fraction.denominator/greatest_common_divisor)
    )


def add(left: Union[int, Fraction], right: Union[int, Fraction]):
    return _simplify_fraction(
        _add_fractions(
            _coerce_into_fraction(left),
            _coerce_into_fraction(right),
        )
    )


def _coerce_into_fraction(number: Union[int, Fraction]):
    if isinstance(number, int):
        return Fraction(number, 1)
    else:
        return number


def _add_fractions(left: Fraction, right: Fraction):
    return Fraction(
        left.numerator * right.denominator + right.numerator * left.denominator,
        left.denominator * right.denominator
    )


class DenominatorIsZero(Exception):
    pass
