import argparse
from pathlib import Path
from typing import NamedTuple

from src.preprocessors.base import PreprocessorBase
from src.preprocessors.math_aps import MathAPSPreprocessor, MathAPSTreePreprocessor


class Args(NamedTuple):
    """
    Stores cli arguments.

    Attributes:
      dataset_type: One of math-aps, and math-aps-tree
      file: Path to the original dataset
      step_tag: Step tag to be appended to each step
      suffix: Suffix to be appended to `file` for the output path
    """

    dataset_type: str
    file: Path
    step_tag: str
    suffix: str = "new"


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dataset_type",
        type=str,
        help="Which dataset FILE is (math-aps, or math-aps-tree)",
    )
    parser.add_argument(
        "file",
        type=Path,
        help="Path to the original dataset file",
    )
    parser.add_argument(
        "-t",
        "--step-tag",
        type=str,
        help=r"Step tag. Default: \n\n\n\n\n",
        default="\n\n\n\n\n",
    )
    parser.add_argument(
        "-s",
        "--suffix",
        type=str,
        help="Suffix appended to FILE for the output path. Default: new",
        default="new",
    )

    return Args(**vars(parser.parse_args()))


def main(args: Args) -> None:
    runner_args = {
        "ds_path": args.file,
        "step_tag": args.step_tag,
        "suffix": args.suffix,
    }

    runner: PreprocessorBase
    runner = {
        "math-aps": MathAPSPreprocessor,
        "math-aps-tree": MathAPSTreePreprocessor,
    }[args.dataset_type](**runner_args)
    runner.convert()
    runner.dump()


if __name__ == "__main__":
    main(parse_args())
