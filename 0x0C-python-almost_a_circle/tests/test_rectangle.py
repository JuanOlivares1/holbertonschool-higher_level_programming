#!usr/bin/python3
"""Test module for 'rectangle'"""
import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """Test class for ´Rectangle´ class"""
    r1 = Rectangle(10, 2)
    r2 = Rectangle(2, 10)
    r3 = Rectangle(10, 2, 0, 0, 12)
    r4 = Rectangle(3, 2)
    r5 = Rectangle(2, 10)
    r6 = Rectangle(8, 7, 0, 0, 15)

    def test_construc(self):
        """test the correct construction of instances"""
        self.assertEqual(test_rectangle.r1.id, 1)
        self.assertEqual(test_rectangle.r2.id, 2)
        self.assertEqual(test_rectangle.r3.id, 12)
        self.assertEqual(test_rectangle.r4.id, 3)
        self.assertEqual(test_rectangle.r5.id, 4)
        self.assertEqual(test_rectangle.r6.id, 15)

    def test_exception(self):
        """test the correct rasing of exceptions"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 3.1416)
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r = Rectangle(10, [1, 3, 4])

        with self.assertRaises(TypeError):
            r = Rectangle(3.1416, 10)
        with self.assertRaises(TypeError):
            r = Rectangle("2", 10)
        with self.assertRaises(TypeError):
            r = Rectangle([1, 3, 4], 10)

        with self.assertRaises(ValueError):
            r = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(10, -1)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 10)

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 4, -1)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -1, 4)

    def test_area(self):
        """test area function"""
        self.assertEqual(test_rectangle.r1.area(), 20)
        self.assertEqual(test_rectangle.r2.area(), 20)
        self.assertEqual(test_rectangle.r3.area(), 20)
        self.assertEqual(test_rectangle.r4.area(), 6)
        self.assertEqual(test_rectangle.r5.area(), 20)
        self.assertEqual(test_rectangle.r6.area(), 56)
