class Fraction:

    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    def __str__(self):
        return "({} / {})".format(self.num, self.denum)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        return Fraction(num, denum)

    def __sub__(self, other):
        num = self.num * other.denum - other.num * self.denum
        denum = self.denum * other.denum
        return Fraction(num, denum)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denum * other.denum)

    def __truediv__(self, other):
        return Fraction(self.num * other.denum, self.denum * other.num)

    def __eq__(self, other):
        return self.num / self.denum == other.num / other.denum

