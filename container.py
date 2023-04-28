from copy import deepcopy
from typing import Any, List


# A generic type that is meant to be one and the same in each usage
T = Any

_container: List[T] = []


def push(item: T):
    _container.append(item)


def get_last_copied() -> T:
    return deepcopy(_container[-1])


def pop():
    _container.pop()
