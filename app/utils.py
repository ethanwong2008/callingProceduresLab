"""
Utility procedures student implement and test.
"""

# This import is important later to understand what's going on
from typing import Dict, Optional

def add(a: float, b: float) -> float:
    return a + b


def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number with fib(0) == 0, fib(1) == 1.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



"""
Simple "database"
Hi again! We imported `typing.Dict` because it's more readable type wise.
That is, so you can tell what we types of variables (string, integer, etc.) we want to use in our dictionary.
"""
_DB: Dict[str, Dict] = {}

def create_item(key: str, value: Dict) -> None:
    """
    Create or replace an item at key with value.
    """
    _DB[key] = value

def read_item(key: str) -> Optional[Dict]:
    """
    Return a copy of the stored dict or None if absent.
    """
    value = _DB.get(key)
    return value.copy() if value is not None else None

def update_item(key: str, patch: Dict) -> bool:
    """
    Update a stored dictionary item with the keys/values from patch.
    Return True if item exists and was updated, False if item missing.
    """
    if key not in _DB:
        return False
    _DB[key].update(patch)
    return True

def delete_item(key: str) -> bool:
    """
    Delete item at key. Return True if deleted, False if item missing.
    """
    if key in _DB:
        del _DB[key]
        return True
    return False

def clear_db() -> None:
    """Helper for tests (remove all items)."""
    global _DB
    _DB = {}
