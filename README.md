# Adaptive Drift Monitor

Small, dependency-free streaming monitor for production ML features. It combines a rolling robust z-score with Page-Hinkley change detection and emits JSON alerts suitable for a queue or metrics adapter.

## Run

```bash
python -m drift_monitor --values 10,11,10,12,80,82
python -m unittest discover -s tests -v
```

The implementation is intentionally stdlib-only so the detector can run beside an inference service without a numerical runtime.

## Senior engineering notes

This detector is designed for online inference paths where a dependency-free signal is useful. Before production, persist state across restarts, tune thresholds on a labeled stream, attach model and feature metadata to alerts, and measure alert precision so paging remains actionable.
