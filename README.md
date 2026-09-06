# Adaptive Drift Monitor

Small, dependency-free streaming monitor for production ML features. It combines a rolling robust z-score with Page-Hinkley change detection and emits JSON alerts suitable for a queue or metrics adapter.

## Run

```bash
python -m drift_monitor --values 10,11,10,12,80,82
python -m unittest discover -s tests -v
```

The implementation is intentionally stdlib-only so the detector can run beside an inference service without a numerical runtime.
