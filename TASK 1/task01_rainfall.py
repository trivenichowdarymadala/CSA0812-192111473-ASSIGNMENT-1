"""Q1: Daily rainfall analysis using lists and slicing."""
import random

def moving_average_naive(values, window=7):
    if window <= 0:
        raise ValueError("window must be positive")
    return [sum(values[i:i + window]) / window
            for i in range(len(values) - window + 1)]

def moving_average_running(values, window=7):
    if window <= 0:
        raise ValueError("window must be positive")
    if len(values) < window:
        return []
    current = sum(values[:window])
    result = [current / window]
    for i in range(window, len(values)):
        current += values[i] - values[i - window]
        result.append(current / window)
    return result

def analyse_rainfall(readings):
    weekly_totals = [sum(readings[i:i+7]) for i in range(0, len(readings), 7)]
    if readings:
        maximum = (max(readings), readings.index(max(readings)))
        minimum = (min(readings), readings.index(min(readings)))
    else:
        maximum = minimum = None
    dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]
    return weekly_totals, maximum, minimum, moving_average_running(readings), dry_days

if __name__ == "__main__":
    random.seed(42)
    rainfall = [round(random.uniform(0, 25), 2) for _ in range(365)]
    rainfall[4] = 0
    rainfall[100] = 0
    weekly, high, low, averages, dry = analyse_rainfall(rainfall)
    print("Number of days:", len(rainfall))
    print("First five weekly totals:", weekly[:5])
    print("Maximum (mm, zero-based index):", high)
    print("Minimum (mm, zero-based index):", low)
    print("First five 7-day averages:", [round(x, 2) for x in averages[:5]])
    print("Dry days (1-based day numbers):", dry)
