import function
import unittest
class TestModule (unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(function.discriminant(1,2,1), (0))
        self.assertEqual(function.discriminant(1, 1, 1), (-3))
        self.assertEqual(function.discriminant(10, -1, -1), (41))
    def test_roots(self):
        self.assertEqual(function.roots(4, 3, 4, 1), (-0.3333333333333333, -1.0))
        self.assertEqual(function.roots(0,1,2,1),(-1))
        self.assertEqual(function.roots(-8,1,2,3),(-1 + 1.4142135623730951j, -1 - 1.4142135623730951j))