from typing import Union

import math


class Fraction(object):
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        if denominator == 0:
            raise DenominatorIsZero()
        self.denominator = denominator

    def __eq__(self, other):
        return (self.numerator == other.numerator
                and self.denominator == other.denominator)

    def __repr__(self):
        return "{numerator}/{denominator}".format(
            numerator=self.numerator, denominator=self.denominator
        )


def _simplify_fraction(fraction: Fraction):
    greatest_common_divisor = math.gcd(fraction.numerator, fraction.denominator)
    return Fraction(
        fraction.numerator/greatest_common_divisor,
        fraction.denominator/greatest_common_divisor
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
