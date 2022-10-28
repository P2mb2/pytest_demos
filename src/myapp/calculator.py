import json
from typing import Any


def add(a: Any, b: Any) -> Any:
    return a + b


def divide(a: Any, b: Any) -> Any:
    return a / b


def add_only_ints(a: int, b: int) -> Any:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input values must be integers")
    return add(a + b)


def add_and_save_file(a: Any, b: Any, filepath: str) -> None:
    json.dump({"a": a, "b": b, "result": add(a, b)}, open(filepath, 'w'))


def add_and_print_console(a: Any, b: Any) -> None:
    print(f'{a} + {b} = {add(a, b)}')
