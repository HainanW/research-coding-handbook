# 01 — Run and debug Python scripts in VS Code

<!-- print:omit -->
[Handbook](../README.md) · [English–Chinese edition](01-main-running-and-debugging.zh-CN.md) · [Bilingual PDF](print/01-main-running-and-debugging.zh-CN.pdf)
<!-- /print:omit -->

## 1. Run the example

Open the repository folder in VS Code. Use **Ctrl+Shift+P → Python: Select Interpreter** to select an installed Python environment. The interpreter executes your code. You need the Microsoft Python and Python Debugger extensions.

Open [the chapter 10 script](../examples/10_python_annotations_and_parsing.py), save it, then choose **Run Python File in Terminal** from the upper-right triangle. This example needs Python 3.9+ and only the standard library. See [VS Code: running Python](https://code.visualstudio.com/docs/python/run).

Expected output:

```text
p value: {'rho': 50.0}
p type: dict
annotation: dict[str, float] | None
annotation type: str
output path: None
```

Alternatively, run this in a PowerShell terminal at the repository root:

```powershell
python examples/10_python_annotations_and_parsing.py
```

If the prompt is `>>>`, enter `exit()` first to leave the Python interactive session.

## 2. Pause and inspect a function

### 2.1 Do I need to enter arguments first?

No extra input is needed for the current example: the caller already supplies the argument. These excerpts are from the chapter 10 script:

```python
from __future__ import annotations

# Function definition
def identity(p: dict[str, float] | None = None):
    return p

# Inside main()
p = {"rho": 50.0}
value = identity(p)
```

A **parameter** is the receiving name in a function definition; an **argument** is what the caller supplies. Here, `p` receives the dictionary. Because its default is `None`, calling `identity()` returns `None`. Required parameters without defaults must receive arguments; the debugger does not prompt for them.

Here, `--output-dir` is an optional command-line argument, separate from the function argument. Omitting it leaves `args.output_dir` as `None`; `identity` still receives the dictionary. The script does not call `input()` or wait for keyboard input.

### 2.2 Follow the argument into the function

Keep the example `.py` file active. Click the gutter next to `value = identity(p)` to add a breakpoint. Start debugging with `F5`; if prompted, choose **Python Debugger** and the current Python file. If an existing launch configuration targets another program, choose the current-file configuration instead. See [Python debugging](https://code.visualstudio.com/docs/python/debugging).

At the breakpoint, the highlighted statement has not executed yet. On this fresh run, `p` is `{'rho': 50.0}`, while `value` has not been assigned. Press **Step Into** (`F11`) to enter `identity`. At `return p`, its local parameter `p` refers to that same dictionary.

```python
p          # {'rho': 50.0}
type(p)    # <class 'dict'>
p["rho"]   # 50.0
```

Enter these expressions separately in Debug Console while paused inside `identity`. Terminal is for shell commands or keyboard input requested by the program. They inspect the argument already received; they do not supply a missing argument. Use **Shift+F11** to return to the caller, then **F5** to continue after inspecting the completed assignment.

| Windows default action | What it does |
| --- | --- |
| F10 — Step Over | Execute the current line without entering its function calls; other breakpoints can still interrupt. |
| F11 — Step Into | Enter a called function when supported by the debugger. |
| Shift+F11 — Step Out | Finish the current function and return to its caller. |
| F5 — Continue | Resume until another breakpoint, a configured exception stop, or completion. |
| Shift+F5 — Stop | End the debugging session. |

## 3. Prepare inputs for a debugging session

First identify how the program receives its input. For this learning example, start with a fixed input in `main()` so that you can repeat the same run and compare values.

| Input source | How to supply it while debugging |
| --- | --- |
| A function call such as `identity(test_p)` | Create `test_p` before the call. |
| A command-line option such as `--output-dir` | Set `args` in the selected `launch.json` configuration. |
| An interactive `input()` call | Type in Terminal when the running program requests input. |

### 3.1 Fixed arguments in a small caller

This is a standalone teaching variant, not a replacement for the chapter 10 script. It uses only the standard library. Save it as a separate practice `.py` file if you want to run it:

```python
def identity(p=None):
    return p


def main():
    test_p = {"rho": 60.0}
    result = identity(test_p)  # Set a breakpoint here
    print(result)


if __name__ == "__main__":
    main()
```

Start this practice file under the debugger, pause at the call, and press F11. In `main`, the argument is named `test_p`; inside `identity`, the receiving parameter is named `p`. The names can differ. Both refer to the same dictionary, and the final output is `{'rho': 60.0}`. Change `test_p` and restart to try a different input. Calling `identity()` instead returns `None` because this function has a default.

### 3.2 Command-line inputs in launch.json

For the existing chapter 10 script, the following configuration supplies the option `--output-dir results/demo`. This is a configuration example; documenting it does not change your VS Code settings. In `.vscode/launch.json`, add the configuration object to the existing `configurations` list, or use the whole file below if none exists:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Chapter 10: arguments",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/examples/10_python_annotations_and_parsing.py",
            "cwd": "${workspaceFolder}",
            "console": "integratedTerminal",
            "args": ["--output-dir", "results/demo"]
        }
    ]
}
```

Open the repository root as the VS Code workspace. Select **Chapter 10: arguments** in Run and Debug, then press F5. `program` fixes the script, `cwd` fixes the working directory, and `args` supplies script options. The final output is `output path: results/demo`; no directory is created. Each token is a separate `args` item. See [Python debugging](https://code.visualstudio.com/docs/python/debugging).

This configuration always targets chapter 10, even when a different file is open. Switch back to a current-file configuration to debug the practice variant in section 3.1. `--output-dir` does not set `p` or `rho`: the script only connects this option to `args.output_dir`. Passing a value into `identity` still requires a Python function call.

### 3.3 Interactive keyboard input

For an interactive variant of section 3.1, keep its `identity` definition and entry-point guard, but replace the body of `main()` with:

```python
    rho = float(input("Enter rho: "))
    p = {"rho": rho}
    value = identity(p)  # Set a breakpoint here
    print(value)
```

Debug that practice file with the integrated terminal. When the prompt appears, select **Terminal**, type `60`, and press Enter. The program converts the text to `60.0`, builds the dictionary, and then reaches the breakpoint. Entering expressions in Debug Console does not answer this terminal prompt. Nonnumeric text fails at `float(...)` with `ValueError`, before the function call.

## Verification and next discussion

The original script and both practice variants were checked with Python 3.13.9. Fixed input and interactive input `60` both printed `{'rho': 60.0}`. The default call `identity()` returned `None`. The JSON example was parsed and its configured program and arguments were run from the repository root; the VS Code F5 launch itself was not performed.

Next, we can add exception breakpoints and traceback reading based on your own debugging session. [01-SI](01-SI-spyder.md) preserves the more detailed Spyder array-inspection example.
