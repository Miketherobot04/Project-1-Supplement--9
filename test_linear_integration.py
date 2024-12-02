import unittest
from linear_integration import integrate_linear_function

class TestLinearIntegration(unittest.TestCase):
    def test_positive_slope(self):
        result = integrate_linear_function((2, 3), 0, 5)
        self.assertAlmostEqual(result, 42.5, places=2)

    def test_negative_slope(self):
        result = integrate_linear_function((-1, 4), 1, 3)
        self.assertAlmostEqual(result, 4, places=2)

if __name__ == "__main__":
    unittest.main()