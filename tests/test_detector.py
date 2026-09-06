import unittest
from drift_monitor import DriftDetector

class DetectorTests(unittest.TestCase):
    def test_spike_alert(self):
        d = DriftDetector(window=5, z_threshold=3)
        for x in [1, 1, 1, 1]: self.assertIsNone(d.update(x))
        self.assertEqual(d.update(20).reason, "robust_z")

    def test_rejects_nan(self):
        with self.assertRaises(ValueError): DriftDetector().update(float("nan"))

if __name__ == "__main__": unittest.main()
