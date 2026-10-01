# 10 — Python imports, type annotations, and parsing

<!-- print:omit -->
[Handbook](../README.md)
<!-- /print:omit -->

## The question

What do S1 imports, `from __future__ import annotations`, and `parse` mean in the WO Table 4 script?

This guide uses `Code_Python_rogp39/Case2-WO-Table4-Reproduction/wo_eq36_fullscan_IK_casadi.py`. The small examples explain Python behavior; they do not run the process model. The version-specific behavior below was checked with Python 3.9.25.

## 1. Type annotations describe expected data

```python
def square(x: float) -> float:
    return x * x
```

`x: float` describes the expected input type. `-> float` describes the expected return type. The calculation is still `x * x`. Python does not automatically enforce these hints or convert the data: `square(3)` returns the integer `9`. See [Python type hints](https://docs.python.org/3.9/library/typing.html).

In the WO script, read this parameter one piece at a time:

```python
p: dict[str, float] | None = None
```

| Part | Meaning |
| --- | --- |
| `p` | Parameter name |
| `dict[str, float]` | Dictionary with string keys and float values, such as `{"rho": 50.0}` |
| `\| None` | The type hint also allows `None` |
| `= None` | If the caller omits `p`, its default value is `None` |

Likewise, `sc: list[dict[str, Any]]` describes a list of scenario dictionaries. `Any` leaves value types unrestricted; a record can contain float flows and integer indices. `-> np.ndarray` describes an array return value.

## 2. Why the future import is needed here

Without the future import, Python 3.9 tries to evaluate `dict[str, float] | None` while defining the function, before any call. It can parse the expression, but cannot perform this type-union operation, so it raises `TypeError`. Type unions using `|` were added in [Python 3.10](https://docs.python.org/3.10/whatsnew/3.10.html#pep-604-new-type-union-operator).

```python
from __future__ import annotations

def identity(p: dict[str, float] | None = None):
    return p

print(identity({"rho": 50.0}))       # {'rho': 50.0}
print(type(identity.__annotations__["p"]).__name__)  # str
```

`identity.__annotations__["p"]` retrieves the stored annotation for `p`. With the future statement, Python 3.9 stores it as the text `"dict[str, float] | None"`, avoiding evaluation at function definition. Only the annotation becomes text; the supplied `p` remains a dictionary. This does not add runtime support for type unions if another tool later evaluates that text. See [PEP 563](https://peps.python.org/pep-0563/).

`__future__` is a special standard-library module. Python recognizes `from __future__ import annotations` as an instruction to enable this annotation behavior in the file. *Dunder* means *double underscore*: `__future__` has two underscores at each end. Put the statement before ordinary imports; a module docstring and comments may precede it. See [future statements](https://docs.python.org/3.9/reference/simple_stmts.html#future-statements).

## 3. Read the S1 imports by their job

S1 makes tools available. These import lines do not start the WO optimization.

| Import | Use in this script |
| --- | --- |
| `import argparse` | Read options such as `--output-dir` |
| `import csv` | Read historical MATLAB results and write result/comparison tables |
| `from datetime import datetime, timezone` | Record UTC dates and create timestamped run names |
| `import hashlib` | Record SHA-256 file fingerprints for source tracking |
| `import json` | Save configuration, versions, and run records |
| `from pathlib import Path` | Locate files, build paths, and create output directories |
| `import platform` | Record the Python version |
| `import time` | Measure solver elapsed time with `perf_counter()` |
| `from typing import Any` | Supply `Any` for type annotations |
| `import casadi as ca` | Build symbolic variables, objectives, and constraints; call IPOPT |
| `import numpy as np` | Work with numerical arrays, initial guesses, and results |

`import csv` gives names such as `csv.DictWriter`. `from pathlib import Path` allows `Path(...)` directly. `as np` gives NumPy a short name. These are three common import forms.

```python
V = ca.MX.sym("V")  # Symbolic decision variable
V0 = np.array([60.0])  # Numerical initial value
```

These two lines require the CasADi and NumPy imports above. CasADi represents the optimization model; NumPy handles numerical data. Later, `ca.nlpsol(..., "ipopt", ...)` selects IPOPT as the solver.

## 4. Parse means read according to rules

When parsing Python text such as `a = 1 + 2`, a parser identifies an assignment and an addition. Executing it calculates `3` and assigns it to `a`.

In this script, `parser.parse_args()` instead reads command-line options and stores their values in `args`. The options `--output-dir` and `--historical-csv` become `args.output_dir` and `args.historical_csv`; omitted options are `None`. Here `type=Path` actually converts a supplied value to a path object; it is not a type annotation. See [argparse](https://docs.python.org/3.9/library/argparse.html).

Run the [small standalone example](../examples/10_python_annotations_and_parsing.py) from the handbook root. It requires Python 3.9+ and no external packages; it creates no output directory or simulation results.

```text
python examples/10_python_annotations_and_parsing.py --output-dir results/demo
```

Expected output:

```text
p value: {'rho': 50.0}
p type: dict
annotation: dict[str, float] | None
annotation type: str
output path: results/demo
```

The dictionary is unchanged, its type annotation is stored as text, and the command-line path has been read. The real WO script then passes that path to `run_sweep()` to begin its calculations.
