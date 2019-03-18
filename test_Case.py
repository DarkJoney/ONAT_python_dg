import unittest

from calcfunc import calc2
from calcfunc import calc3


class NamesTestingRRR(unittest.TestCase):
    """FFFFF"""
    def test_two_values(self):
        """GGGG"""
        calculated = calc2(6, 7)
        self.assertEqual(calculated, 13)

    def test_three_values(self):
        """hhhh"""
        calculated = calc2(1, 2, 3)
        self.assertEqual(calculated, 6)


unittest.main()





