from argparse import ArgumentParser
from contextlib import contextmanager
import importlib
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("day", type=int)
parser.add_argument("part", choices=("a", "b"))
parser.add_argument("input")

argv = parser.parse_args()
module = f"day{argv.day:02d}"

input_aliases = {"s": "sample", "i": "input"}


@contextmanager
def open_file():
    file_name = argv.input
    if file_name in input_aliases:
        file_name = input_aliases[file_name]

    with open(Path(__file__).parent / module / f"{file_name}.txt") as f:
        yield f


def main():
    importlib.import_module(f"aoc2025.{module}.{argv.part}")
