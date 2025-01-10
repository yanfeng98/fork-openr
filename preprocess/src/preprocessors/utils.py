import json
from pathlib import Path
from typing import Iterable

from src.data_types import (ConvertedItem, MathAPSItem, MathAPSItemTree)


def read_math_aps_ds(ds_path: Path) -> Iterable[MathAPSItem]:
    with open(ds_path, "r", encoding="utf-8") as fd:
        dict_lst = map(json.loads, fd.readlines())

    return map(MathAPSItem.from_dict, dict_lst)


def read_math_aps_tree_ds(ds_path: Path) -> Iterable[MathAPSItemTree]:
    with open(ds_path, "r", encoding="utf-8") as fd:
        dict_lst = map(json.loads, fd.readlines())

    return map(MathAPSItemTree.from_dict, dict_lst)


def dump_converted_ds(save_path: Path, items: list[ConvertedItem]) -> None:
    with open(save_path, "w", encoding="utf-8") as fd:
        json.dump([it.to_dict() for it in items], fd)
