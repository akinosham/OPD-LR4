import unittest
from trigonometry import calculate_trigonometry


class TestTrigonometry(unittest.TestCase):

    def test_sin_radians(self):
        self.assertAlmostEqual(calculate_trigonometry(30, 'sin', 'radians'), -0.988, delta=0.0001)

    def test_sin_degrees(self):
        self.assertAlmostEqual(calculate_trigonometry(45, 'sin', 'degrees'), 0.7071, delta=0.0001)

    def test_cos_radians(self):
        self.assertAlmostEqual(calculate_trigonometry(60, 'cos', 'radians'), -0.9524, delta=0.0001)

    def test_cos_degrees(self):
        self.assertAlmostEqual(calculate_trigonometry(30, 'cos', 'degrees'), 0.866, delta=0.001)

    def test_tan_radians(self):
        self.assertAlmostEqual(calculate_trigonometry(45, 'tan', 'radians'), 1.62, delta=0.01)

    def test_tan_degrees(self):
        self.assertAlmostEqual(calculate_trigonometry(0, 'tan', 'degrees'), 0, delta=0.0001)


if __name__ == '__main__':
    unittest.main()