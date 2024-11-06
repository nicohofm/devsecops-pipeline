import unittest
from app2 import calculation


class TestApp1(unittest.TestCase):
    def test_some_function(self):
        a = 5
        b = 6
        self.assertEqual(calculation(a, b), 11)


if __name__ == '__main__':
    unittest.main()
