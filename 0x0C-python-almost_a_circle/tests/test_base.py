#!usr/bin/python3
"""Test module for 'base'"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """Test class for ´Base´ class"""
    def test_construc(self, id=None):
        """test the correct construction of instances"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        b5 = Base(34)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 34)
