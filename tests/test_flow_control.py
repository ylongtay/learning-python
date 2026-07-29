import unittest
from src.flow_control.leap_year_checker import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2004))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2021))
        self.assertTrue(is_leap_year(2024))

if __name__ == '__main__':
    unittest.main()
