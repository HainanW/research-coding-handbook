# 10 — Python imports, type annotations, and parsing / Python 导入、类型标注与解析

<!-- bilingual: en-zh -->

<!-- print:omit -->
[Handbook / 返回手册](../README.zh-CN.md) · [English](10-main-python-imports-annotations-parsing.md)
<!-- /print:omit -->

## The question / 问题

What do S1 imports, `from __future__ import annotations`, and `parse` mean in the WO Table 4 script?

WO Table 4 脚本中的 S1 导入、`from __future__ import annotations` 和 `parse` 分别是什么意思？

This guide uses `Code_Python_rogp39/Case2-WO-Table4-Reproduction/wo_eq36_fullscan_IK_casadi.py`. The small examples explain Python behavior; they do not run the process model. The version-specific behavior below was checked with Python 3.9.25.

本文对应 `Code_Python_rogp39/Case2-WO-Table4-Reproduction/wo_eq36_fullscan_IK_casadi.py`。小例子只演示 Python 行为，不运行工艺模型。下面涉及版本的行为已用 Python 3.9.25 核对。

## 1. Type annotations describe expected data / 类型标注说明预期的数据类型

```python
def square(x: float) -> float:
    return x * x
```

`x: float` describes the expected input type. `-> float` describes the expected return type. The calculation is still `x * x`. Python does not automatically enforce these hints or convert the data: `square(3)` returns the integer `9`. See [Python type hints](https://docs.python.org/3.9/library/typing.html).

`x: float` 说明预期输入是浮点数；`-> float` 说明预期返回浮点数。实际计算仍是 `x * x`。Python 不会自动按标注检查或转换数据：`square(3)` 仍返回整数 `9`。参见 [Python 类型提示](https://docs.python.org/3.9/library/typing.html)。

In the WO script, read this parameter one piece at a time:

把 WO 脚本中的这个参数拆开看：

```python
p: dict[str, float] | None = None
```

| Part<br>部分 | Meaning<br>含义 |
| --- | --- |
| `p` | Parameter name<br>参数名 |
| `dict[str, float]` | Dictionary with string keys and float values, such as `{"rho": 50.0}`<br>键是字符串、值是浮点数的字典，如 `{"rho": 50.0}` |
| `\| None` | The type hint also allows `None`<br>类型说明也允许 `None` |
| `= None` | If the caller omits `p`, its default value is `None`<br>调用时不提供 `p`，默认值就是 `None` |

Likewise, `sc: list[dict[str, Any]]` describes a list of scenario dictionaries. `Any` leaves value types unrestricted; a record can contain float flows and integer indices. `-> np.ndarray` describes an array return value.

同理，`sc: list[dict[str, Any]]` 表示由情景字典组成的列表。`Any` 不限定值的类型，因此一条记录可以同时包含浮点流量和整数编号。`-> np.ndarray` 说明预期返回数组。

## 2. Why the future import is needed here / 这里为什么要用 future import

Without the future import, Python 3.9 tries to evaluate `dict[str, float] | None` while defining the function, before any call. It can parse the expression, but cannot perform this type-union operation, so it raises `TypeError`. Type unions using `|` were added in [Python 3.10](https://docs.python.org/3.10/whatsnew/3.10.html#pep-604-new-type-union-operator).

不加 future import 时，Python 3.9 在定义函数时就会尝试处理 `dict[str, float] | None`，这时还没有调用函数。它能读懂表达式的结构，但还不支持用 `|` 组合类型，因此报 `TypeError`。这种类型联合运算是在 [Python 3.10](https://docs.python.org/3.10/whatsnew/3.10.html#pep-604-new-type-union-operator) 中加入的。

```python
from __future__ import annotations

def identity(p: dict[str, float] | None = None):
    return p

print(identity({"rho": 50.0}))       # {'rho': 50.0}
print(type(identity.__annotations__["p"]).__name__)  # str
```

`identity.__annotations__["p"]` retrieves the stored annotation for `p`. With the future statement, Python 3.9 stores it as the text `"dict[str, float] | None"`, avoiding evaluation at function definition. Only the annotation becomes text; the supplied `p` remains a dictionary. This does not add runtime support for type unions if another tool later evaluates that text. See [PEP 563](https://peps.python.org/pep-0563/).

`identity.__annotations__["p"]` 取出函数保存的 `p` 的类型标注。加上 future 语句后，Python 3.9 把它保存为文字 `"dict[str, float] | None"`，定义函数时不计算它。只有标注变成文字，传入的 `p` 仍是字典。如果其他工具后来再计算这段文字，Python 3.9 仍不因此获得类型联合运算能力。参见 [PEP 563](https://peps.python.org/pep-0563/)。

`__future__` is a special standard-library module. Python recognizes `from __future__ import annotations` as an instruction to enable this annotation behavior in the file. *Dunder* means *double underscore*: `__future__` has two underscores at each end. Put the statement before ordinary imports; a module docstring and comments may precede it. See [future statements](https://docs.python.org/3.9/reference/simple_stmts.html#future-statements).

`__future__` 是特殊的标准库模块。整句 `from __future__ import annotations` 相当于“在本文件开启上述标注处理方式”。dunder 是 double underscore（双下划线）的简称，`__future__` 前后各有两个下划线。这句放在普通导入之前；前面可以有文件说明字符串和注释。参见 [future 语句](https://docs.python.org/3.9/reference/simple_stmts.html#future-statements)。

## 3. Read the S1 imports by their job / 按用途理解 S1 导入

S1 makes tools available. These import lines do not start the WO optimization.

S1 准备后面要用的工具。这些导入语句还没有开始 WO 优化计算。

| Import<br>导入语句 | Use in this script<br>本脚本中的用途 |
| --- | --- |
| `import argparse` | Read options such as `--output-dir`<br>读取 `--output-dir` 等运行选项 |
| `import csv` | Read historical MATLAB results and write result/comparison tables<br>读取 MATLAB 历史结果，写出结果表和比较表 |
| `from datetime import datetime, timezone` | Record UTC dates and create timestamped run names<br>记录 UTC 日期时间，生成带时间戳的运行名称 |
| `import hashlib` | Record SHA-256 file fingerprints for source tracking<br>记录文件的 SHA-256“指纹”，用于追溯来源 |
| `import json` | Save configuration, versions, and run records<br>保存配置、版本和运行记录 |
| `from pathlib import Path` | Locate files, build paths, and create output directories<br>定位文件、拼接路径、创建输出目录 |
| `import platform` | Record the Python version<br>记录 Python 版本 |
| `import time` | Measure solver elapsed time with `perf_counter()`<br>用 `perf_counter()` 计算求解耗时 |
| `from typing import Any` | Supply `Any` for type annotations<br>提供类型标注中的 `Any` |
| `import casadi as ca` | Build symbolic variables, objectives, and constraints; call IPOPT<br>建立符号变量、目标和约束，调用 IPOPT |
| `import numpy as np` | Work with numerical arrays, initial guesses, and results<br>处理数值数组、初值和结果 |

`import csv` gives names such as `csv.DictWriter`. `from pathlib import Path` allows `Path(...)` directly. `as np` gives NumPy a short name. These are three common import forms.

`import csv` 后用 `csv.DictWriter`；`from pathlib import Path` 后直接用 `Path(...)`；`as np` 给 NumPy 起简称。这是三种常见的导入形式。

```python
V = ca.MX.sym("V")  # Symbolic decision variable
V0 = np.array([60.0])  # Numerical initial value
```

These two lines require the CasADi and NumPy imports above. CasADi represents the optimization model; NumPy handles numerical data. Later, `ca.nlpsol(..., "ipopt", ...)` selects IPOPT as the solver.

这两行需要先导入上表中的 CasADi 和 NumPy。`V` 是符号决策变量，`V0` 是含有具体数值的初值数组。CasADi 表达优化模型，NumPy 处理数值数据；后面的 `ca.nlpsol(..., "ipopt", ...)` 指定 IPOPT 求解器。

## 4. Parse means read according to rules / Parse 就是按规则解析

When parsing Python text such as `a = 1 + 2`, a parser identifies an assignment and an addition. Executing it calculates `3` and assigns it to `a`.

解析 Python 文本 `a = 1 + 2` 时，解析器识别出“赋值”和“加法”的结构。执行时才算出 `3`，并把它赋给 `a`。

In this script, `parser.parse_args()` instead reads command-line options and stores their values in `args`. The options `--output-dir` and `--historical-csv` become `args.output_dir` and `args.historical_csv`; omitted options are `None`. Here `type=Path` actually converts a supplied value to a path object; it is not a type annotation. See [argparse](https://docs.python.org/3.9/library/argparse.html).

在本脚本里，`parser.parse_args()` 读取命令行选项，并把值放进 `args`。`--output-dir` 和 `--historical-csv` 分别对应 `args.output_dir` 和 `args.historical_csv`；未提供时为 `None`。这里的 `type=Path` 会实际把传入的值转换成路径对象，它不是类型标注。参见 [argparse](https://docs.python.org/3.9/library/argparse.html)。

Run the [small standalone example](../examples/10_python_annotations_and_parsing.py) from the handbook root. It requires Python 3.9+ and no external packages; it creates no output directory or simulation results.

在手册根目录运行这个[独立小例子](../examples/10_python_annotations_and_parsing.py)。需要 Python 3.9+，无需额外安装库；它不会创建输出目录或生成模拟结果。

```text
python examples/10_python_annotations_and_parsing.py --output-dir results/demo
```

Expected output:

预期输出：

```text
p value: {'rho': 50.0}
p type: dict
annotation: dict[str, float] | None
annotation type: str
output path: results/demo
```

The dictionary is unchanged, its type annotation is stored as text, and the command-line path has been read. The real WO script then passes that path to `run_sweep()` to begin its calculations.

字典保持原样，类型标注保存为文字，命令行路径也已读出。实际 WO 脚本随后把路径传给 `run_sweep()`，才进入计算流程。
