"""
    Skins list logging module.
"""

from skin import SKINS_LIST


def log() -> None:
    for skin in SKINS_LIST:
        print(skin)
    print(len(SKINS_LIST))
