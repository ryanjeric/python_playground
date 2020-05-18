# https://www.youtube.com/watch?v=6tNS--WetLI by Corey Schafer
import unittest
import calc


class TestCalc(unittest.TestCase):
    # always prefix with "text_"
    @classmethod
    def setUpClass(cls):
        print('setup class')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('tearDown')

    def test_add(self):
        print('TEST ADD')
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        print('TEST SUBTRACT')
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        print('TEST MULTIPLY')
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        print('TEST DIVIDE')
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):  # context manager
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
