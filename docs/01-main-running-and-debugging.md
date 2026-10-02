# 01 — Run and debug Python scripts in VS Code

<!-- print:omit -->
[Handbook](../README.md) · [English–Chinese edition](01-main-running-and-debugging.zh-CN.md) · [Bilingual PDF](print/01-main-running-and-debugging.zh-CN.pdf)
<!-- /print:omit -->

## Question and example

How do I run the open Python file, pass options, and pause inside a function to inspect its values? This first edition uses the existing [chapter 10 script](../examples/10_python_annotations_and_parsing.py). It needs Python 3.9+ and only the standard library. It prints values and does not create files. The original Spyder tutorial is now [01-SI — Spyder](01-SI-spyder.md), supplementary information for this chapter.

## 1. Choose the interpreter

Open the repository folder in VS Code. Confirm that Microsoft's Python and Python Debugger extensions are available. An editor displays your code; the Python interpreter executes it.

Press `Ctrl+Shift+P`, run **Python: Select Interpreter**, and choose an installed environment. The selected interpreter is normally used for Python runs and debugging; a debug configuration can override it. See [VS Code: environments](https://code.visualstudio.com/docs/python/environments).

In a newly opened terminal, check which interpreter the command `python` actually resolves to:

```powershell
python -c "import sys; print(sys.executable); print(sys.version)"
```

Compare the printed executable with your selection. An already-open terminal can still use a previous environment. For environment setup, see [chapter 07](07-main-conda-environment.md).

## 2. Run the open file

Open `examples/10_python_annotations_and_parsing.py`, save it, and choose **Run Python File in Terminal** from the upper-right play button. Inspect the command and output in **Terminal**. If another extension supplies a similar triangle, identify the Python command by its label. See [VS Code: running Python](https://code.visualstudio.com/docs/python/run).

Running executes the script to completion unless it waits for input or encounters an error. A breakpoint only pauses execution when a debugger is attached. For this example, running without options produces:

```text
p value: {'rho': 50.0}
p type: dict
annotation: dict[str, float] | None
annotation type: str
output path: None
```

`None` here means no output path was supplied; it is not an error. The meanings of the annotation and `__name__` guard are explained in [chapter 10](10-main-python-imports-annotations-parsing.md).

## 3. Run from the terminal and pass an option

At a PowerShell prompt, with the repository root as the current directory, run:

```powershell
Get-Location
python examples/10_python_annotations_and_parsing.py
python examples/10_python_annotations_and_parsing.py --output-dir results/demo
```

The second Python command changes the final output to `output path: results/demo`. In this teaching script the path is parsed and printed; no directory is created. `python` selects the interpreter, the `.py` path selects the script, and `--output-dir results/demo` supplies a script option.

The current working directory determines how relative paths are interpreted. It is not necessarily the script's folder. A prompt beginning with `>>>` is a Python REPL; enter `exit()` before typing these PowerShell commands.

## 4. Pause and inspect a function

Keep the example `.py` file active. Click the gutter next to `value = identity(p)` to add a breakpoint. Start debugging with `F5`; if prompted, choose **Python Debugger** and the current Python file. If an existing launch configuration targets another program, choose the current-file configuration instead. See [Python debugging](https://code.visualstudio.com/docs/python/debugging).

At the breakpoint, the highlighted statement has not executed yet. On this fresh run, `p` is `{'rho': 50.0}`, while `value` has not been assigned. Press **Step Into** (`F11`) to enter `identity`. At `return p`, its local parameter `p` refers to that same dictionary.

Inspect `p`, `type(p)`, and `p["rho"]` in **Debug Console** while paused; the results are the dictionary, `dict`, and `50.0`. After returning to `main`, use Step Over if needed until the assignment has finished. Then `value` is available and `value is p` is `True`: this function returns the original object, not a copy.

| Windows default action | What it does |
| --- | --- |
| F10 — Step Over | Execute the current line without entering its function calls; other breakpoints can still interrupt. |
| F11 — Step Into | Enter a called function when supported by the debugger. |
| Shift+F11 — Step Out | Finish the current function and return to its caller. |
| F5 — Continue | Resume until another breakpoint, a configured exception stop, or completion. |
| Shift+F5 — Stop | End the debugging session. |

**Variables**, **Watch**, and **Call Stack** help inspect the paused state. The selected stack frame determines the available local variables. See [VS Code: debugging controls](https://code.visualstudio.com/docs/debugtest/debugging). Shortcuts can be customized; use toolbar labels if yours differ.

## 5. Keep the three consoles distinct

| Location | What to enter |
| --- | --- |
| Terminal with a PowerShell prompt | Shell commands, including `python script.py`. |
| Python REPL with `>>>` | Python statements, in that REPL's own session. |
| Debug Console during a paused session | Expressions for the selected frame, such as `p["rho"]`. |

A separately launched script's local variables do not automatically appear in a different Python REPL after it exits. Pause before the function returns to inspect them.

If the file is not found, check the working directory and script path. If a module is missing, check the interpreter and its dependencies. If a breakpoint does not stop, check that you started debugging, selected the correct script, and reached that executable line.

## Verification and next discussion

The two terminal runs above were executed with Python 3.13.9 and produced the displayed values. The VS Code steps were checked against official documentation; the graphical debug session has not been performed here.

Next, we can work through your own pause-and-step session, then add saved arguments in `launch.json`, exception breakpoints, and traceback reading as needed. This chapter starts with the basic run/debug workflow; [01-SI](01-SI-spyder.md) preserves the more detailed Spyder array-inspection example.
