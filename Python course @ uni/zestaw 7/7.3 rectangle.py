from points import Point
import random

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

        if x1 > x2 or y1 > y2:
            raise ValueError('Bad input')

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)
        return f'Rectangle {self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y}'

    def __eq__(self, other):    # obsługa rect1 == rect2
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        else: return False

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return (self.pt1.x + self.pt2.x) /2, (self.pt1.y + self.pt2.y) / 2

    def area(self):             # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        return self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y

    def intersection(self, other):  # część wspólna prostokątów
        if self.pt1.x < other.pt1.x < self.pt2.x and self.pt1.y < other.pt1.y < self.pt2.y \
            and (other.pt2.x > self.pt2.x or other.pt2.y > self.pt2.y):
            return f'{other.pt1}, {self.pt2}'

        elif other.pt1.x < self.pt1.x < other.pt2.x and self.pt1.y < other.pt1.y < self.pt2.y:
            return f'{self.pt1.x, other.pt1.y}, {other.pt2.x, self.pt2.y}'

        elif other.pt1.x < self.pt1.x < other.pt2.x and other.pt1.y < self.pt1.y <other.pt2.y \
            and (self.pt2.x > other.pt2.x or self.pt2.y > other.pt2.y):
            return f'{self.pt1}, {other.pt2}'

        elif self.pt1.x < other.pt1.x < self.pt2.x and self.pt1.y < other.pt2.y < self.pt2.y\
            and other.pt2.x > self.pt2.x :
            return f'{other.pt1.x, self.pt1.y}, {self.pt2.x, other.pt2.y}'

        elif other.pt1.x <= self.pt1.x and other.pt1.y <= self.pt1.y and self.pt2.x <= other.pt2.x\
            and self.pt2.y <= other.pt2.y:
            return f'{self.pt1}, {self.pt2}'

        elif self.pt1.x <= other.pt1.x and self.pt1.y <= other.pt1.y and other.pt2.x <= self.pt2.x \
            and other.pt2.y <= self.pt2.y:
            return f'{other.pt1}, {other.pt2}'

    def cover(self, other):   # prostąkąt nakrywający oba
        return f'{min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y)}, ' \
               f'{max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y)}'

    def make4(self):        # zwraca krotkę czterech mniejszych
        lista = []
        for i in range(8):
           lista.append((random.randint(self.pt1.x, self.pt2.x), random.randint(self.pt1.y, self.pt2.y)))
        return tuple(lista)


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(1,1,3,3)
        self.rect2 = Rectangle(2,2,5,5)
        self.rect3 = Rectangle(-1,2,2,5)
        self.rect4 = Rectangle(-1,-1,2,2)
        self.rect5 = Rectangle(2,-1,5,2)
        self.rect6 = Rectangle(0,0,0,0)
        self.rect7 = Rectangle(1, 1, 3, 3)
        self.rect8 = Rectangle(0, 0, 5, 5)


    def test_init(self):
        with self.assertRaises(ValueError):
            self.__init__(Rectangle(5,5,2,2))

    def test_str(self):
        self.assertEqual(self.rect1.__str__(), "[(1, 1), (3, 3)]")

    def test_repr(self):
        self.assertEqual(self.rect1.__repr__(), 'Rectangle (1, 1, 3, 3)')

    def test_eq(self):
        self.assertTrue(self.rect1.__eq__(self.rect7))

    def test_ne(self):
        self.assertTrue(self.rect1.__ne__(self.rect5))

    def test_center(self):
        self.assertEqual(self.rect1.center(), (2.0, 2.0))
        self.assertEqual(self.rect4.center(), (0.5, 0.5))
        self.assertEqual(self.rect6.center(), (0, 0))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 4)
        self.assertEqual(self.rect4.area(), 9)
        self.assertEqual(self.rect6.area(), 0)

    def test_move(self):
        self.assertEqual(self.rect1.move(1, 1), (2, 2, 4, 4))
        self.assertEqual(self.rect4.move(1, 1), (0, 0, 3, 3))
        self.assertEqual(self.rect6.move(1, 1), (1, 1, 1, 1))

    def test_intersection(self):
        self.assertEqual(self.rect1.intersection(self.rect2), ('(2, 2), (3, 3)'))
        self.assertEqual(self.rect1.intersection(self.rect3), ('(1, 2), (2, 3)'))
        self.assertEqual(self.rect1.intersection(self.rect4), ('(1, 1), (2, 2)'))
        self.assertEqual(self.rect1.intersection(self.rect5), ('(2, 1), (3, 2)'))
        self.assertEqual(self.rect1.intersection(self.rect6), (None))
        self.assertEqual(self.rect1.intersection(self.rect7), ('(1, 1), (3, 3)'))
        self.assertEqual(self.rect1.intersection(self.rect8), ('(1, 1), (3, 3)'))
        self.assertEqual(self.rect8.intersection(self.rect1), ('(1, 1), (3, 3)'))

    def test_cover(self):
        self.assertEqual(self.rect1.cover(self.rect2), '(1, 1), (5, 5)')
        self.assertEqual(self.rect1.cover(self.rect4), '(-1, -1), (3, 3)')
        self.assertEqual(self.rect1.cover(self.rect6), '(0, 0), (3, 3)')


if __name__ == '__main__':
    unittest.main()