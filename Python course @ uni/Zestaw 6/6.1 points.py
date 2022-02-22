import unittest

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):       # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self):         # zwraca string "Point(x, y)"
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):    # obsługa point1 == point2
        return True if self.x == other.x and self.y == other.y else False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return (self.x * self.x + self.y * self.y)**0.5

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.
# pkt = Point(3, 4)
# inny = Point(5, 6)
# print(pkt.__ne__(inny))

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.pkt1 = Point(3, 4)
        self.pkt2 = Point(3, 4)
        self.pkt3 = Point(1, 2)
        self.pkt4 = Point(0, 0)
        self.pkt5 = Point(-3,-4)

    def test_str(self):
        self.assertEqual(self.pkt1.__str__(), '(3, 4)')
        self.assertEqual(self.pkt4.__str__(), '(0, 0)')
        self.assertEqual(self.pkt5.__str__(), '(-3, -4)')

    def test_repr(self):
        self.assertEqual(self.pkt1.__repr__(), 'Point(3, 4)')
        self.assertEqual(self.pkt4.__repr__(), 'Point(0, 0)')
        self.assertEqual(self.pkt5.__repr__(), 'Point(-3, -4)')

    def test_eq(self):
        self.assertTrue(self.pkt1.__eq__(self.pkt2))
        self.assertFalse(self.pkt1.__eq__(self.pkt4))
        self.assertFalse(self.pkt1.__eq__(self.pkt5))

    def test_ne(self):
        self.assertTrue(self.pkt1.__ne__(self.pkt3))
        self.assertFalse(self.pkt1.__ne__(self.pkt2))

    def test_add(self):
        self.assertEqual(self.pkt1.__add__(self.pkt3), Point(4, 6))
        self.assertEqual(self.pkt1.__add__(self.pkt5), Point(0, 0))
        self.assertEqual(self.pkt1.__add__(self.pkt4), Point(3, 4))

    def test_sub(self):
        self.assertEqual(self.pkt1.__sub__(self.pkt2), Point(0, 0))
        self.assertEqual(self.pkt1.__sub__(self.pkt5), Point(6, 8))
        self.assertEqual(self.pkt1.__sub__(self.pkt4), Point(3, 4))

    def test_mul(self):
        self.assertEqual(self.pkt1.__mul__(self.pkt3), 11)
        self.assertEqual(self.pkt1.__mul__(self.pkt4), 0)
        self.assertEqual(self.pkt1.__mul__(self.pkt5), -25)

    def test_cross(self):
        self.assertEqual(self.pkt1.cross(self.pkt3), 2)
        self.assertEqual(self.pkt1.cross(self.pkt5), 0)
        self.assertEqual(self.pkt1.cross(self.pkt4), 0)

    def test_length(self):
        self.assertEqual(self.pkt1.length(), 5)
        self.assertEqual(self.pkt4.length(), 0)
        self.assertEqual(self.pkt5.length(), 5)

    def test_hash(self):
        self.assertEqual(self.pkt1.__hash__(), hash(Point(3, 4)))

if __name__ == '__main__':
    unittest.main()