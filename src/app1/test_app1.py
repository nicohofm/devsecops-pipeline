import unittest
from app1 import hello


class TestApp1(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello, "Hello, DevSecOps!")


if __name__ == '__main__':
    unittest.main()
