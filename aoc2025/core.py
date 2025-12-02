from argparse import ArgumentParser
from contextlib import contextmanager
import importlib
from os import listdir
import os
from pathlib import Path
import re

parser = ArgumentParser()

sub_parsers = parser.add_subparsers(dest="command", required=True)

run_parser = sub_parsers.add_parser("run")
run_parser.add_argument("day", type=int)
run_parser.add_argument("part", choices=("a", "b"))
run_parser.add_argument("input")

new_group = sub_parsers.add_parser("new")

argv = parser.parse_args()

module_dir = Path(__file__).parent

script_template = """from ..core import open_file


with open_file() as f:
    ...
"""


def new():
    max_day = 1
    for d in listdir(module_dir):
        if re.match(r"day\d\d", d):
            max_day = max(max_day, int(d.removeprefix("day")))
    new_day = max_day + 1
    new_module = f"day{new_day:02d}"
    os.makedirs(module_dir / new_module)
    with open(module_dir / new_module / "a.py", "w") as f:
        f.write(script_template)
    with open(module_dir / new_module / "sample.txt", "w"):
        ...
    with open(module_dir / new_module / "input.txt", "w"):
        ...


def run():
    module = f"day{argv.day:02d}"
    importlib.import_module(f"aoc2025.{module}.{argv.part}")


input_aliases = {"s": "sample", "i": "input"}


@contextmanager
def open_file():
    assert argv.command == "run"
    file_name = argv.input
    if file_name in input_aliases:
        file_name = input_aliases[file_name]

    with open(Path(__file__).parent / f"day{argv.day:02d}" / f"{file_name}.txt") as f:
        yield f


def main():
    match argv.command:
        case "run":
            run()
        case "new":
            new()
