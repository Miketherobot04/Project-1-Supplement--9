import unittest
from generate_samples import generate_normal_samples

class TestGenerateSamples(unittest.TestCase):
    def test_sample_generation(self):
        samples = generate_normal_samples(0, 1, 1000)
        self.assertEqual(len(samples), 1000)
        self.assertAlmostEqual(sum(samples) / len(samples), 0, delta=0.1)

if __name__ == "__main__":
    unittest.main()