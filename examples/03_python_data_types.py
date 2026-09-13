"""Q3: Python data types and a Case 1 profit equation.
Run with Python 3.9+ and NumPy. In Spyder, run cells in order.
Small inputs below are teaching data, not the paper's optimized solution.
"""
import math
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import numpy as np


# %% 1. Built-in values: inspect samples, then individual names
count = 3
noise_std = 0.12
impedance = 2 + 3j
converged = True
label = "Case 1"
quantities = [1.0, 2.0, 3.0]
bounds = (0.0, 6.0)
indices = range(3)
settings = {"noise_std": noise_std, "seed": 5}
unique_ids = {1, 2, 2}
fixed_ids = frozenset({1, 2})
payload = b"ABC"
buffer = bytearray(b"ABC")
view = memoryview(buffer)
missing = None
samples = {
    "int": count, "float": noise_std, "complex": impedance,
    "bool": converged, "str": label, "list": quantities,
    "tuple": bounds, "range": indices, "dict": settings,
    "set": unique_ids, "frozenset": fixed_ids, "bytes": payload,
    "bytearray": buffer, "memoryview": view, "NoneType": missing,
}
for name, value in samples.items():
    length = len(value) if hasattr(value, "__len__") else "N/A"
    print(f"{name:12s} type={type(value).__name__:12s} len={length}")

# %% 2. Access, conversion, and mutation
first_quantity = quantities[0]
upper_bound = bounds[1]
first_index = indices[0]
configured_seed = settings["seed"]
contains_two = 2 in unique_ids
first_byte = payload[0]                 # integer 65, not 'A'
view[0] = 90                           # buffer becomes bytearray(b'ZBC')
parsed_float = float("0.12")
truncated = int(3.9)                    # 3, not rounding
single_tuple = (3,)                     # comma matters
alias = quantities
independent = quantities.copy()         # shallow copy
alias[0] = 9.0                         # quantities changes too
nested_tuple = ([1, 2], "fixed slots")
nested_tuple[0].append(3)               # contained list remains mutable

# %% 3. NumPy: container type versus element dtype
array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
array_scalar = array[0, 0]              # np.float64 scalar
python_scalar = array_scalar.item()    # Python float
zero_dim = np.array(0.12)               # shape (), size 1; len() invalid
array_view = array[:, :2]               # shares storage
array_copy = array.copy()              # independent numeric storage
print("array:", type(array), array.dtype, array.shape, array.size)
print("scalar types:", type(array_scalar), type(python_scalar))


# %% 4. Original Case 1 functions (S6.1)
def true_price_fn(x):
    x = np.asarray(x, dtype=float)
    return np.exp(-x / 2.0)


def realized_profit_samples(x, noise_matrix, cost_vec):
    x = np.asarray(x, dtype=float).reshape(1, -1)
    cost_vec = np.asarray(cost_vec, dtype=float).reshape(1, -1)
    realized_price = true_price_fn(x) + noise_matrix
    # P1: break here to inspect x, cost_vec, noise_matrix, realized_price.
    return np.sum(x * (realized_price - cost_vec), axis=1)


# %% 5. Four scenarios, three production components
x_input = [1.0, 2.0, 3.0]
cost_input = (0.1, 0.2, 0.3)
noise_matrix = np.array([
    [0.00, 0.00, 0.00],
    [0.10, 0.00, -0.10],
    [-0.10, 0.10, 0.00],
    [0.02, -0.03, 0.04],
], dtype=float)
profits = realized_profit_samples(x_input, noise_matrix, cost_input)
print("profits =", np.round(profits, 8))
print("profit shape =", profits.shape)

# A loop evaluates the same equation without broadcasting.
reference = []
for row in noise_matrix:
    total = 0.0
    for j, quantity in enumerate(x_input):
        price = math.exp(-quantity / 2.0) + float(row[j])
        total += quantity * (price - cost_input[j])
    reference.append(total)
np.testing.assert_allclose(profits, reference, rtol=1e-12, atol=1e-12)
assert profits.shape == (4,)
# Revenue changes linearly with each scenario's noise at fixed production.
np.testing.assert_allclose(profits - profits[0], [0, -0.2, 0.1, 0.08])

# %% 6. Further objects encountered in research code
exact_decimal = Decimal("0.1") + Decimal("0.2")
exact_fraction = Fraction(1, 3)
output_path = Path("results") / "profits.csv"  # no file is written
function_object = true_price_fn
module_object = np
class_object = float
iterator = iter([1, 2, 3])
generator = (i * i for i in range(3))
selection = slice(0, 2)
problem = ValueError("example only; not raised")
ellipsis_value = Ellipsis
not_implemented_value = NotImplemented
print("Verification passed.")
