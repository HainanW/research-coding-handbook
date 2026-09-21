# 05 — Python dunder methods and special names

<!-- print:omit -->
[Back to the handbook](../README.md)

[PDF](print/05-main-python-dunder.pdf) · [Print HTML](print/05-main-python-dunder.html)
<!-- /print:omit -->

## The question

> What does dunder mean, and how do I use names such as `__init__`, `__len__`, and `__name__` in Python?

Dunder is short for double underscore. Names such as `__init__` have two underscores at each end. Distinguish special methods from special attributes or module variables: `__len__` is a method, whereas a module's `__name__` is a string.

## 1. Connect familiar operations to special methods

When using an object, normally write `len(x)` or `x[0]`. When writing your own class, implement the appropriate special methods to support those operations. These method names are part of Python's protocols; do not invent new dunder names for ordinary helpers.

| Operation | Special method | Purpose |
| --- | --- | --- |
| Initialize an instance | `__init__` | Set initial attributes |
| `print(x)`, `str(x)` | `__str__` | Human-readable text |
| `repr(x)` | `__repr__` | Debugging representation |
| `len(x)` | `__len__` | Number of items |
| `x[0]` | `__getitem__` | Index or key lookup |
| `x + y` | `__add__` | Addition behavior |
| `x == y` | `__eq__` | Equality comparison |
| `iter(x)` | `__iter__` | Supply an iterator |
| `x()` | `__call__` | Make an instance callable |

This table is a lookup aid, not a literal expansion of every expression. Operators may involve reflected methods or fallbacks. For example, addition can also consider `__radd__`. Implicit special-method lookup generally uses the object's type, so attaching a method only to an individual instance is not a reliable way to support `len(instance)`.

## 2. A small class for scenario profits

The numbers below are illustrative rounded profits, not a new Case 1 calculation. Save or run [the complete example](../examples/05_dunder_methods.py); it requires Python 3.9+ and no external packages.

```python
class ProfitSamples:
    def __init__(self, values):
        self.values = list(values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __repr__(self):
        return f"ProfitSamples({self.values!r})"

```

Now create an instance and inspect it:

```python
profits = ProfitSamples([0.61, 0.41, 0.71])
print(len(profits))       # 3
print(profits[0])         # 0.61
print(profits)            # ProfitSamples([0.61, 0.41, 0.71])
```

Read our class one method at a time:

- `__init__` stores the supplied values in a list. It initializes an already created instance; object creation is handled by `__new__`. An initializer must not return a non-`None` value.
- `self` refers to the current instance. It is a conventional parameter name, not a keyword or a dunder name. Python supplies it when a bound method is called.
- `__len__` delegates to the stored list, so this instance reports three items.
- `__getitem__` delegates to that list, so index 0 returns `0.61`. In this implementation, `profits[:2]` returns a list, not another `ProfitSamples` instance.
- `__repr__` includes the class name and stored values. The `!r` in the f-string uses `repr(self.values)`. Our class does not override `__str__`, so printing it falls back to this representation.

In Spyder, put a breakpoint on `return len(self.values)` and debug the script. When `len(profits)` reaches the breakpoint, inspect `type(self)`, `self.values`, and `type(self.values)`. This connects the custom instance with the ordinary list it contains.

## 3. The script entry point: `__name__`

Our example ends with:

```python
def main():
    profits = ProfitSamples([0.61, 0.41, 0.71])
    print(len(profits))
    print(profits[0])
    print(profits)


if __name__ == "__main__":
    main()
```

Here `__name__` is a module variable, not a method. Running the file directly gives it the value `"__main__"`, so the demonstration runs. Loading it as an imported module with a different name leaves the guarded call unexecuted. Importing still executes other top-level statements, including class and function definitions; the guard protects only its own block.

From the repository root:

```powershell
python examples/05_dunder_methods.py
```

Expected output:

```text
3
0.61
ProfitSamples([0.61, 0.41, 0.71])
```

For a normal file named `experiment.py`, `import experiment` sets that module's `__name__` to `"experiment"`; package imports can use a dotted name such as `"package.experiment"`. The handbook example's numeric filename is convenient for ordering, so use `importlib` if you want to import it by path rather than writing a normal import statement starting with a digit.

## 4. Similar underscore patterns have different meanings

| Pattern | Meaning |
| --- | --- |
| `value` | Ordinary name |
| `_value` | Convention for internal use, not access control |
| `__value` inside a class | Name mangling to reduce subclass name collisions |
| `__value__` | Form used for documented special names |

For example, a class `Demo` with `self.__value = 1` normally stores it under `_Demo__value`. This is not a security boundary. `__init__` has trailing double underscores and is not a private method.

## 5. What to learn first

Start with `__init__`, `__repr__`, `__len__`, `__getitem__`, and the `__name__` guard. You do not need a custom class just to calculate profits with NumPy. A class becomes useful when related data and operations should travel together.

Try predicting `profits[-1]`, `profits[:2]`, and `type(profits.values)`. For this class, the answers are `0.71`, `[0.61, 0.41]`, and `list`. The built-in list provides the indexing rules because our implementation delegates to it.

## Sources

See Python's [special-method reference](https://docs.python.org/3/reference/datamodel.html#special-method-names) for protocol details and its [top-level code environment guide](https://docs.python.org/3/library/__main__.html) for the entry-point guard. The `ProfitSamples` example and inspection exercise are specific to this handbook.
