from typing import Union


class Fraction(object):
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return (self.numerator == other.numerator
                and self.denominator == other.denominator)

    def __repr__(self):
        return "{numerator}/{denominator}".format(
            numerator=self.numerator, denominator=self.denominator
        )


def add(left: Union[int, Fraction], right: Union[int, Fraction]):
    return _add_fractions(
        _coerce_into_fraction(left),
        _coerce_into_fraction(right),
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
