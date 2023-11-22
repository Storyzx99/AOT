#Testing titan classgit 
#import unittest
import unittest
from unittest import TestCase
from classes import *

class TestTitan(TestCase):

    def testHealthLetter(self):
        with self.assertRaises(AssertionError):
            test_titan = Titan(name = "Test", health = "a", power = 10)


