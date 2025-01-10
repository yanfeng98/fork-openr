from typing import Any, Callable, Type, TypeVar, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    """Manual type check for `str`."""
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    """
    Manual type check for `int`.

    `isinstance` treats `bool` as `int`, so we need to explicitly exclude `bool`.
    """
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    """
    Manual type check for `float`.

    Include `int` (which will be casted to `float`) but exclude `bool`.
    """
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_list(f: Callable[[Any], T], x: Any) -> list[T]:
    """
    Assert `x` is a list and call `f` on elements of `x`.

    Can be used for type checking each element of `x`.
    """
    assert isinstance(x, list)
    return list(map(f, x))


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return float(x)


def to_dict(c: Type[T], x: Any) -> dict:
    """Convert `x` of class `c` to dict. `c` should have the method `to_dict`."""
    assert isinstance(x, c)
    return cast(Any, x).to_dict()
