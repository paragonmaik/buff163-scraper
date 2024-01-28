"""
    Flags reading module.
"""

import sys
from typing import Any, List


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
]

USED_COMMANDS_LIST = {}


# TODO: return dict with the flag as key to access the value
def read_flags() -> dict:

    for i, flag in enumerate(sys.argv):
        for command in COMMANDS_LIST:
            if flag == command.short_flag:
                command.value = sys.argv[i + 1]
                USED_COMMANDS_LIST[command.short_flag] = (
                    command.value
                )
                # print(i, flag, command.value)
    print(USED_COMMANDS_LIST)

    return USED_COMMANDS_LIST
