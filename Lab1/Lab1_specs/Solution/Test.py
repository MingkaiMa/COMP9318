import unittest
import Q1
import Q1_v2
from math import sqrt, floor

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.n = 2
        self.n1 = Q1.nsqrt(self.n)
        self.n2 = Q1_v2.nsqrt(self.n)

    def test(self):
        self.assertEqual(self.n1, floor(sqrt(self.n)))
        self.assertEqual(self.n2, floor(sqrt(self.n)))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)