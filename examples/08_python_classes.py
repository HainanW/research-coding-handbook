"""08: Classes, instance state, and aliases using teaching measurements.

Requires Python 3.9+; no external dependencies.
Run from the repository root: python examples/08_python_classes.py
In Spyder, run the numbered cells in order or debug at P1.
These values illustrate Python behavior, not real experimental results.
"""

from math import isclose


# %% 1. Define a type for one experiment run
class ExperimentRun:
    """Keep a name and a flat numeric measurement list in milliseconds."""

    unit = "ms"

    def __init__(self, name, measurements):
        self.name = name
        self.measurements = list(measurements)

    def add_measurement(self, value):
        self.measurements.append(value)

    def mean(self):
        if not self.measurements:
            raise ValueError("Cannot calculate a mean without measurements.")
        # P1: inspect self.name and self.measurements before calculating.
        return sum(self.measurements) / len(self.measurements)


# %% 2. Create records and inspect independent lists
source = [10.0, 12.0]
run_a = ExperimentRun("run A", source)
run_b = ExperimentRun("run B", source)
run_a.add_measurement(14.0)
source.append(99.0)


# %% 3. Calculate and print hand-checkable results
mean_a = run_a.mean()
mean_b = run_b.mean()
print(f"{run_a.name}: {run_a.measurements}, mean = {mean_a:.1f} {run_a.unit}")
print(f"{run_b.name}: {run_b.measurements}, mean = {mean_b:.1f} {run_b.unit}")
print(f"source: {source}")
print(f"same instance: {run_a is run_b}")
print(f"same measurement list: {run_a.measurements is run_b.measurements}")


# %% 4. An empty record has no mean; handle the expected error
empty_run = ExperimentRun("empty run", [])
try:
    empty_run.mean()
except ValueError as error:
    print(f"empty run: {error}")
else:
    raise AssertionError("An empty record should raise ValueError.")


# %% 5. Verify arithmetic and the intended boundaries between objects
assert isclose(mean_a, 12.0)
assert isclose(mean_b, 11.0)
assert run_a is not run_b
assert run_a.measurements is not run_b.measurements
assert run_a.measurements == [10.0, 12.0, 14.0]
assert run_b.measurements == [10.0, 12.0]
assert source == [10.0, 12.0, 99.0]
assert run_a.measurements is not source
assert run_b.measurements is not source

# Assignment adds a reference to an existing instance; it does not copy it.
alias = run_a
assert alias is run_a
print("Verification passed.")
