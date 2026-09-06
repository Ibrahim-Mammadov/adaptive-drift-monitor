import argparse, json
from .detector import DriftDetector

def main():
    p = argparse.ArgumentParser(); p.add_argument("--values", required=True)
    a = p.parse_args(); d = DriftDetector()
    for v in a.values.split(","):
        alert = d.update(float(v))
        if alert: print(json.dumps(alert.__dict__))
if __name__ == "__main__": main()
