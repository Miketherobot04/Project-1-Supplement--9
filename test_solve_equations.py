import unittest
from solve_equations import solve_system_of_equations

class TestSolveEquations(unittest.TestCase):
    def test_two_equations(self):
        equations = [
            lambda vars: vars[0] + vars[1] - 5,
            lambda vars: vars[0] - vars[1] + 1
        ]
        result = solve_system_of_equations(equations, (0, 0))
        self.assertAlmostEqual(result["X"], 2, places=2)
        self.assertAlmostEqual(result["Y"], 3, places=2)

if __name__ == "__main__":
    unittest.main()