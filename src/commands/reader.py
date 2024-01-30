"""
    Flags reading module.
"""

import sys
from typing import Any

# TODO: add help command that prints COMMANDS_LIST to the
# terminal


class Command:
    def __init__(
        self,
        short_flag: str,
        long_flag: str,
        description: str,
    ) -> None:
        self.short_flag = short_flag
        self.long_flag = long_flag
        self.description = description

    short_flag: str = ""
    long_flag: str = ""
    description: str = ""
    value: Any = None


COMMANDS_LIST = [
    Command(
        "-v",
        "--value",
        "Filters item by price difference based on value passed.",
    ),
    Command(
        "-p",
        "--percentage",
        "Filters item by percentage difference based on value passed.",
    ),
    Command(
        "-q",
        "--quantity",
        "Filters item by ask quantity based on value passed.",
    ),
    Command(
        "-b",
        "--bid",
        "Filters item by bid quantity based on value passed.",
    ),
    Command(
        "-w",
        "--wear",
        "Filters item by skin wear, excluding skins with the value passed.",
    ),
]

USED_COMMANDS_LIST = {}


def read_flags() -> None:
    for i, flag in enumerate(sys.argv):
        for command in COMMANDS_LIST:
            if flag == command.short_flag:
                command.value = sys.argv[i + 1]
                USED_COMMANDS_LIST[command.short_flag] = (
                    command.value
                )
    print(USED_COMMANDS_LIST)
