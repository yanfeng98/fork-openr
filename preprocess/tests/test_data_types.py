import json
from pathlib import Path

import pytest
from src.data_types.math_aps import MathAPSItem, MathAPSItemTree

TEST_DIR = Path(__file__).parent.resolve()


@pytest.fixture(scope="module")
def example_prm800k_path() -> Path:
    return TEST_DIR / "samples_prm800k.jsonl"


@pytest.fixture(scope="module")
def example_math_aps_path() -> Path:
    return TEST_DIR / "samples_math-aps.jsonl"


@pytest.fixture(scope="module")
def example_math_shepherd_path() -> Path:
    return TEST_DIR / "samples_math-shepherd.jsonl"


@pytest.fixture(scope="module")
def example_math_aps_tree_path() -> Path:
    return TEST_DIR / "samples_math-aps-tree.jsonl"


def test_math_aps_item(example_math_aps_path: Path) -> None:
    with open(example_math_aps_path, "r") as fd:
        item = MathAPSItem.from_dict(json.loads(fd.readline()))

    print(item)
    assert True


def test_math_aps_item_tree(example_math_aps_tree_path: Path) -> None:
    with open(example_math_aps_tree_path, "r") as fd:
        item = MathAPSItemTree.from_dict(json.loads(fd.readline()))

    print(item)
    assert True
