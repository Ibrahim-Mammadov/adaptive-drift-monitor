import unittest
from drift_monitor import DriftDetector

class DetectorTests(unittest.TestCase):
    def test_spike_alert(self):
        d = DriftDetector(window=5, z_threshold=3)
        for x in [1, 1, 1, 1]: self.assertIsNone(d.update(x))
        self.assertEqual(d.update(20).reason, "robust_z")

    def test_rejects_nan(self):
        with self.assertRaises(ValueError): DriftDetector().update(float("nan"))

    def test_rejects_infinity(self):
        with self.assertRaises(ValueError): DriftDetector().update(float("inf"))

    def test_robust_score_detects_outlier(self):
        d = DriftDetector(window=5, z_threshold=4)
        for x in [1, 1, 1]: self.assertIsNone(d.update(x))
        self.assertEqual(d.update(100).reason, "robust_z")
        self.assertEqual(d.update(20).reason, "robust_z")

if __name__ == "__main__": unittest.main()
