
def add(left, right):
    return left+right


class Fraction(object):
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return (self.numerator == other.numerator
                and self.denominator == other.denominator)
