
def add(left, right):
    if isinstance(left, Fraction) and isinstance(right, Fraction):
        return Fraction(
            left.numerator * right.denominator + right.numerator * left.denominator,
            left.denominator * right.denominator
        )
    if isinstance(right, Fraction):
        return Fraction(
            left * right.denominator + right.numerator,
            right.denominator
        )
    if isinstance(left, Fraction):
        return Fraction(
            right * left.denominator + left.numerator,
            left.denominator
        )
    return left+right


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
