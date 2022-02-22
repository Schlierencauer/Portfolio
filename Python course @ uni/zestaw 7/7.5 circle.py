from points import Point
import math

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return f'Circle{self.pt.x, self.pt.y, self.radius}'

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):            # pole powierzchni
        return math.pi*self.radius**2

    def move(self, x, y):    # przesuniecie o (x, y)
        return self.pt.x + x, self.pt.y + y

    # def cover(self, other):    # najmniejszy okrąg pokrywający oba
    #     return (math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2) + self.radius
    #     + other.radius)/2

circ1 = Circle(0,0,10)
print(circ1.area())
# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):

    def setUp(self):
       self.circ1 = Circle(0, 0, 10)
       self.circ2 = Circle(0, 0, 10)
       self.circ3 = Circle(1, 2, 3)


    def test_init(self):
        with self.assertRaises(ValueError):
            self.__init__(Circle (0,0, -1))

    def test_repr(self):
        self.assertEqual(self.circ1.__repr__(), "Circle(0, 0, 10)")

    def test_eq(self):
        self.assertTrue(self.circ1.__eq__(self.circ2))
        self.assertFalse(self.circ1.__eq__(self.circ3))

    def test_ne(self):
        self.assertFalse(self.circ1.__ne__(self.circ2))
        self.assertTrue(self.circ1.__ne__(self.circ3))

    def test_area(self):
        self.assertEqual(self.circ1.area(), 314.1592653589793)

    def test_move(self):
        self.assertEqual(self.circ1.move(2,2), (2,2))

if __name__ == "__main__":
    unittest.main()