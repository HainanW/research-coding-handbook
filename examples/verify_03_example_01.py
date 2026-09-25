"""Verify example 03-01 without changing its source or writing solver files.

Run from the handbook root: python examples/verify_03_example_01.py
Dependencies: the example's pandas, pyomo, and highspy; standard library otherwise.
Sequential cells simulate shared-namespace execution, not an actual Spyder GUI test.
"""

import argparse
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
import hashlib
from importlib.metadata import PackageNotFoundError, version
import io
import json
from pathlib import Path
import platform
import re
import runpy
import sys
from unittest.mock import patch

import highspy
import pyomo.environ as pyo
from pyomo.core.base.PyomoModel import ModelSolutions


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "examples/03_example_01_mo_book_production.py"
DEFAULT_OUTPUT = ROOT / "examples/results/03-example-01-mo-book-production-verification.json"
TOLERANCE = 1e-6
VALUE_NAMES = {
    "u_units": "y_U", "v_units": "y_V", "material_grams": "x_M",
    "labor_a_hours": "x_A", "labor_b_hours": "x_B",
    "revenue": "revenue", "cost": "cost", "profit": "profit",
}


def portable_path(path):
    """Use repository-relative paths; never publish personal absolute paths."""
    resolved = Path(path).resolve()
    try:
        return resolved.relative_to(ROOT).as_posix() or "."
    except ValueError:
        return "<outside-handbook>/" + resolved.name


def package_version(name):
    try:
        return version(name)
    except PackageNotFoundError:
        return None


def snapshot(namespace):
    """Keep numerical residuals, including slack signs, not just pass flags."""
    model = namespace.get("model")
    result = namespace.get("results")
    output = {
        "solver_status": str(result.solver.status) if result is not None else None,
        "termination_condition": (
            str(result.solver.termination_condition) if result is not None else None
        ),
        "solver_solution_count": len(result.solution) if result is not None else None,
        "values": {}, "source_checks": {}, "constraint_residuals": {},
        "variable_bounds": {}, "tables": {},
    }
    if model is None:
        return output
    for name, component in VALUE_NAMES.items():
        value = pyo.value(getattr(model, component), exception=False)
        output["values"][name] = None if value is None else float(value)
    for constraint in model.component_data_objects(pyo.Constraint, active=True):
        body = pyo.value(constraint.body, exception=False)
        lower = pyo.value(constraint.lower, exception=False)
        upper = pyo.value(constraint.upper, exception=False)
        output["constraint_residuals"][constraint.name] = {
            "body": body, "lower": lower, "upper": upper,
            "body_minus_lower": None if body is None or lower is None else body - lower,
            "upper_minus_body": None if body is None or upper is None else upper - body,
        }
    for variable in model.component_data_objects(pyo.Var):
        output["variable_bounds"][variable.name] = {
            "value": variable.value, "lower": variable.lb, "upper": variable.ub,
            "value_minus_lower": (
                None if variable.value is None or variable.lb is None
                else variable.value - variable.lb
            ),
            "upper_minus_value": (
                None if variable.value is None or variable.ub is None
                else variable.ub - variable.value
            ),
        }
    if "checks" in namespace:
        output["source_checks"] = {key: bool(value) for key, value in namespace["checks"].items()}
    for name in ("production", "resources"):
        if name in namespace:
            output["tables"][name] = json.loads(namespace[name].to_json(orient="records"))
    if "financials" in namespace:
        output["tables"]["financials"] = namespace["financials"].to_dict()
    return output


def execute(source_text, mode="memory", replacement=None):
    namespace = {"__name__": "__main__", "__file__": SOURCE.as_posix()}
    stdout, stderr = io.StringIO(), io.StringIO()
    load_calls = []
    original_load = ModelSolutions.load_from
    error = None
    cell_count = None

    def track_load(solution_store, *args, **kwargs):
        load_calls.append("ModelSolutions.load_from")
        return original_load(solution_store, *args, **kwargs)

    with redirect_stdout(stdout), redirect_stderr(stderr), patch.object(
        ModelSolutions, "load_from", track_load
    ):
        try:
            if replacement:
                old, new = replacement
                if source_text.count(old) != 1:
                    raise ValueError(f"Expected exactly one source substitution: {old}")
                source_text = source_text.replace(old, new, 1)
            if mode == "runpy":
                namespace = runpy.run_path(str(SOURCE), run_name="__main__")
            elif mode == "sequential_cells":
                cells = re.split(r"(?m)^#\s*%%.*$", source_text)
                cells = [cell for cell in cells if cell.strip()]
                cell_count = len(cells)
                for index, cell in enumerate(cells):
                    exec(compile(cell, f"{SOURCE.name}:cell-{index}", "exec"), namespace)
            else:
                exec(compile(source_text, SOURCE.name, "exec"), namespace)
        except Exception as exc:
            error = {"type": type(exc).__name__, "message": str(exc)}
    return {
        "execution_mode": mode,
        "in_memory_substitution": list(replacement) if replacement else None,
        "cell_count": cell_count,
        "stdout": stdout.getvalue(), "stderr": stderr.getvalue(),
        "error": error, "solution_load_calls": len(load_calls),
        **snapshot(namespace),
    }


def solution_checks(case, expected):
    values = case["values"]
    checks = {
        "no_exception": case["error"] is None,
        "optimal_termination": case["termination_condition"] == "optimal",
        "solution_loaded_once": case["solution_load_calls"] == 1,
        "all_eight_source_checks": (
            len(case["source_checks"]) == 8 and all(case["source_checks"].values())
        ),
    }
    for key, target in expected.items():
        actual = values.get(key)
        checks[f"expected_{key}"] = actual is not None and abs(actual - target) <= TOLERANCE
    residuals = [
        item[key] for item in case["constraint_residuals"].values()
        for key in ("body_minus_lower", "upper_minus_body") if item[key] is not None
    ] + [
        item[key] for item in case["variable_bounds"].values()
        for key in ("value_minus_lower", "upper_minus_value") if item[key] is not None
    ]
    checks["raw_residuals_feasible"] = bool(residuals) and min(residuals) >= -TOLERANCE
    case["expected_values"] = expected
    case["verification_checks"] = checks
    case["passed"] = all(checks.values())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output_path = args.output if args.output is not None else DEFAULT_OUTPUT
    source_bytes = SOURCE.read_bytes()
    source_text = source_bytes.decode("utf-8")
    baseline_values = {
        "u_units": 20.0, "v_units": 60.0, "material_grams": 740.0,
        "labor_a_hours": 80.0, "labor_b_hours": 100.0,
        "revenue": 18000.0, "cost": 15400.0, "profit": 2600.0,
    }
    cases = {"baseline": execute(source_text, mode="runpy")}
    solution_checks(cases["baseline"], baseline_values)
    cases["labor_b_120"] = execute(
        source_text, replacement=("labor_b_limit = 100.0", "labor_b_limit = 120.0")
    )
    solution_checks(cases["labor_b_120"], {
        "u_units": 40.0, "v_units": 40.0, "material_grams": 760.0,
        "labor_a_hours": 80.0, "labor_b_hours": 120.0,
        "revenue": 19200.0, "cost": 16400.0, "profit": 2800.0,
    })
    cases["zero_labor_a"] = execute(
        source_text, replacement=("labor_a_limit = 80.0", "labor_a_limit = 0.0")
    )
    solution_checks(cases["zero_labor_a"], {name: 0.0 for name in VALUE_NAMES})
    cases["sequential_cells"] = execute(source_text, mode="sequential_cells")
    solution_checks(cases["sequential_cells"], baseline_values)
    sequential = cases["sequential_cells"]
    sequential["verification_checks"]["matches_baseline_tables"] = (
        sequential["tables"] == cases["baseline"]["tables"]
    )
    sequential["verification_checks"]["nine_cells_executed"] = sequential["cell_count"] == 9
    sequential["passed"] = all(sequential["verification_checks"].values())

    invalid = execute(
        source_text, replacement=("labor_a_limit = 80.0", "labor_a_limit = -1.0")
    )
    invalid["expected_outcome"] = "Infeasible solve rejected before loading any solution."
    invalid["verification_checks"] = {
        "expected_runtime_error": invalid["error"] is not None
        and invalid["error"]["type"] == "RuntimeError"
        and invalid["error"]["message"] == "No proven optimal solution: infeasible",
        "infeasible_termination": invalid["termination_condition"] == "infeasible",
        "solution_not_loaded": invalid["solution_load_calls"] == 0,
        "all_five_variables_unset": len(invalid["variable_bounds"]) == 5
        and all(item["value"] is None for item in invalid["variable_bounds"].values()),
        "no_result_tables_extracted": not invalid["tables"],
    }
    invalid["passed"] = all(invalid["verification_checks"].values())
    cases["negative_labor_a"] = invalid

    # Independently eliminate resources using the original textbook constants.
    # Positive costs imply profit <= 40 U + 30 V, with equality at minimal use.
    analytic_bound = 20.0 * 80.0 + 10.0 * 100.0
    actual_profit = cases["baseline"]["values"].get("profit")
    unchanged = SOURCE.read_bytes() == source_bytes
    bound_passed = actual_profit is not None and abs(actual_profit - analytic_bound) <= TOLERANCE
    passed = unchanged and bound_passed and all(case["passed"] for case in cases.values())
    report = {
        "schema_version": 1,
        "run_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "command": ["python", portable_path(__file__)] + (
            ["--output", portable_path(output_path)] if args.output is not None else []
        ),
        "working_directory": portable_path(Path.cwd()),
        "path_policy": "Paths relative to handbook root; external personal paths redacted.",
        "environment": {
            "python": platform.python_version(), "implementation": platform.python_implementation(),
            "platform": platform.system(), "machine": platform.machine(),
            "interpreter_filename": Path(sys.executable).name,
            "environment_name": Path(sys.executable).parent.name,
            "packages": {name: package_version(name) for name in (
                "pyomo", "highspy", "pandas", "numpy", "spyder", "spyder-kernels"
            )},
            "highs_solver": highspy.Highs().version(),
        },
        "source": {"path": portable_path(SOURCE), "sha256": hashlib.sha256(source_bytes).hexdigest(),
                   "unchanged_after_verification": unchanged},
        "tolerance": TOLERANCE,
        "residual_convention": "Feasible slacks are nonnegative within tolerance; null means unbounded or unset.",
        "scope": "Textbook LP only. Sequential cells share a Python namespace; no Spyder GUI was tested.",
        "independent_analytic_bound": {
            "unit_contributions": {"U": 270 - 10 * 10 - 50 - 2 * 40,
                                   "V": 210 - 9 * 10 - 50 - 40},
            "derivation": "profit <= 40 U + 30 V = 20(U+V) + 10(2U+V) <= 20*80 + 10*100 = 2600",
            "upper_bound": analytic_bound, "baseline_attains_bound": bound_passed,
        },
        "cases": cases, "passed": passed,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(f"Verification {'PASSED' if passed else 'FAILED'}: {portable_path(output_path)}")
    for name, case in cases.items():
        print(f"  {name}: {'PASS' if case['passed'] else 'FAIL'} ({case['termination_condition']})")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
