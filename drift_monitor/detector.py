from dataclasses import dataclass
from math import isfinite
from statistics import median
from collections import deque

@dataclass(frozen=True)
class Alert:
    index: int
    value: float
    score: float
    reason: str

class DriftDetector:
    def __init__(self, window=30, z_threshold=4.0, delta=0.01, threshold=8.0):
        if window < 3 or z_threshold <= 0 or delta < 0 or threshold <= 0:
            raise ValueError("invalid detector parameters")
        self.window, self.z_threshold = window, z_threshold
        self.delta, self.threshold = delta, threshold
        self.values, self.index, self.mean, self.ph = deque(maxlen=window), -1, 0.0, 0.0

    def update(self, value: float):
        value = float(value)
        if not isfinite(value):
            raise ValueError("value must be finite")
        self.index += 1
        baseline = list(self.values)
        score = 0.0
        if len(baseline) >= 3:
            center = median(baseline)
            mad = median(abs(x - center) for x in baseline)
            scale = 1.4826 * mad or 1e-12
            score = abs(value - center) / scale
        self.values.append(value)
        self.mean += (value - self.mean) / (self.index + 1)
        self.ph = max(0.0, self.ph + value - self.mean - self.delta)
        if score >= self.z_threshold:
            return Alert(self.index, value, score, "robust_z")
        if self.ph >= self.threshold:
            self.ph = 0.0
            return Alert(self.index, value, score, "page_hinkley")
        return None
