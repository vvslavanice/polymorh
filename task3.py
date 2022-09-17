''' Володимир поможет чуть-чуть ''' 


from fractions import Fraction

x = Fraction(1,2)
y = Fraction(1,4)

x + y == Fraction(3,4)

print(x)
print(y)

class Fraction:
    def __init__(self):

        def __add__(self, something):
            return something + (x / y)

        def __sub__(self, something):
            return something - (x/ y)

        def __truediv__(self, something):
            return something / (x/ y)

        def __mul__(self, something):
            return something * (x/ y)

