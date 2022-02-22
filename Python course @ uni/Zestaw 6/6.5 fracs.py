import math
import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        if self.y == 0:
            raise ValueError("Nie mozna dzielić przez zero!")

    def __str__(self):        # zwraca "x/y" lub "x" dla y=1
        return f'{self.x}/{self.y}' if self.y != 1 else f'{self.x}'

    def __repr__(self):       # zwraca "Frac(x, y)"
        return f'Frac({self.x}, {self.y})'

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return True if (self.x / self.y) == (other.x / other.y) else False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return True if (self.x / self.y) < (other.x / other.y) else False

    def __le__(self, other):
        return True if (self.x / self.y) <= (other.x / other.y) else False

    def __gt__(self, other):
        return True if (self.x / self.y) > (other.x / other.y) else False

    def __ge__(self, other):
        return True if (self.x / self.y) >= (other.x / other.y) else False

    def __add__(self, other):   # frac1 + frac2
        return (self.x * other.y + other.x * self.y) \
               / math.gcd((self.x * other.y + other.x * self.y), (self.y * other.y)), \
               (self.y * other.y) / math.gcd((self.x * other.y + other.x * self.y), (self.y * other.y))

    def __sub__(self, other):   # frac1 - frac2
        return (self.x * other.y - other.x * self.y) \
               / math.gcd((self.x * other.y - other.x * self.y), (self.y * other.y)), \
               (self.y * other.y)/math.gcd((self.x * other.y - other.x * self.y), (self.y * other.y))

    def __mul__(self, other):  # frac1 * frac2
        return (self.x * other.x) / math.gcd((self.x * other.x), (self.y * other.y)), \
               (self.y * other.y) / math.gcd((self.x * other.x), (self.y * other.y))

    def __truediv__(self, other):  # frac1 / frac2, Python 3
        if other.x == 0 or other.y == 0:
            raise ValueError("Nie mozna dzielić przez zero!")

        else:
            return (self.x * other.y) / math.gcd((self.x * other.y), (self.y * other.x)), \
                   (self.y * other.x) / math.gcd((self.x * other.y), (self.y * other.x))

    # def __floordiv__(self, other):   # frac1 // frac2, opcjonalnie
    #
    #
    # def __mod__(self, other): pass  # frac1 % frac2, opcjonalnie

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        if self.x == 0:
            raise ValueError("Nie mozna dzielić przez zero!")
        else:
            return Frac(self.y, self.x)

    def __float__(self):      # float(frac)
        return float(self.x/self.y)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

# Kod testujący moduł.


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.frac1 = Frac(1, 2)
        self.frac2 = Frac(1, 2)
        self.frac3 = Frac(3, 4)
        self.frac4 = Frac(1, 4)
        self.frac5 = Frac(-1, 2)
        self.frac6 = Frac(1, -2)
        self.frac7 = Frac(0, 1)
        self.frac8 = Frac(0, 1)

    # def test_init(self):
    #     self

    def test_str(self):
        self.assertEqual(self.frac1.__str__(), '1/2')

    def test_repr(self):
        self.assertEqual(self.frac1.__repr__(), 'Frac(1, 2)')
        self.assertEqual(self.frac5.__repr__(), 'Frac(-1, 2)')
        self.assertEqual(self.frac8.__repr__(), 'Frac(0, 1)')

    def test_eq(self):
        self.assertTrue(self.frac1.__eq__(self.frac2))
        self.assertTrue(self.frac5.__eq__(self.frac6))
        self.assertTrue(self.frac7.__eq__(self.frac8))

    def test_ne(self):
        self.assertTrue(self.frac1.__ne__(self.frac3))
        self.assertTrue(self.frac1.__ne__(self.frac5))
        self.assertTrue(self.frac1.__ne__(self.frac8))

    def test_lt(self):
        self.assertTrue(self.frac1.__lt__(self.frac3))
        self.assertFalse(self.frac1.__lt__(self.frac5))
        self.assertFalse(self.frac1.__lt__(self.frac8))

    def test_le(self):
        self.assertTrue(self.frac1.__le__(self.frac3))
        self.assertFalse(self.frac1.__lt__(self.frac5))
        self.assertFalse(self.frac1.__lt__(self.frac8))

    def test_gt(self):
        self.assertTrue(self.frac1.__gt__(self.frac4))
        self.assertTrue(self.frac1.__gt__(self.frac8))
        self.assertTrue(self.frac1.__gt__(self.frac5))

    def test_ge(self):
        self.assertTrue(self.frac1.__ge__(self.frac4))
        self.assertTrue(self.frac1.__gt__(self.frac4))
        self.assertTrue(self.frac1.__gt__(self.frac8))
        self.assertTrue(self.frac1.__gt__(self.frac5))

    def test_add(self):
        self.assertEqual(self.frac1.__add__(self.frac2), (1, 1))
        self.assertEqual(self.frac1.__add__(self.frac8), (1, 2))
        self.assertEqual(self.frac1.__add__(self.frac5), (0, 1))

    def test_sub(self):
        self.assertEqual(self.frac1.__sub__(self.frac2), (0, 1))
        self.assertEqual(self.frac1.__sub__(self.frac5), (1, 1))
        self.assertEqual(self.frac1.__sub__(self.frac8), (1, 2))

    def test_mul(self):
        self.assertEqual(self.frac1.__mul__(self.frac2), (1, 4))
        self.assertEqual(self.frac1.__mul__(self.frac8), (0, 1))
        self.assertEqual(self.frac1.__mul__(self.frac5), (-1, 4))

    def test_truediv(self):
        self.assertEqual(self.frac1.__truediv__(self.frac2), (1, 1))
        self.assertRaises(ValueError, self.frac1.__truediv__, self.frac8)
        self.assertEqual(self.frac1.__truediv__(self.frac5), (1.0, -1.0))

    def test_pos(self):
        self.assertEqual(self.frac1.__pos__(), Frac(1, 2))
        self.assertEqual(self.frac8.__pos__(), Frac(0, 1))
        self.assertEqual(self.frac5.__pos__(), Frac(-1, 2))

    def test_neg(self):
        self.assertEqual(self.frac1.__neg__(), Frac(-1, 2))
        self.assertEqual(self.frac8.__neg__(), Frac(0, 1))
        self.assertEqual(self.frac5.__neg__(), Frac(1, 2))

    def test_invert(self):
        self.assertEqual(self.frac1.__invert__(), Frac(2, 1))
        self.assertRaises(ValueError, self.frac8.__invert__)

    def test_float(self):
        self.assertEqual(self.frac1.__float__(), 0.5)
        self.assertEqual(self.frac8.__float__(), 0.0)
        self.assertEqual(self.frac5.__float__(), -0.5)

    def test_hash(self):
        self.assertEqual(self.frac1.__hash__(), hash(float(Frac(1, 2))))
        self.assertEqual(self.frac8.__hash__(), hash(float(Frac(0, 1))))
        self.assertEqual(self.frac5.__hash__(), hash(float(Frac(-1, 2))))


if __name__ == "__main__":
    unittest.main()
