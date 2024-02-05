"""
    Skins list logging module.
"""

from skin import SKINS_LIST


def log() -> None:
    if len(SKINS_LIST) > 0:
        for skin in SKINS_LIST:
            print(skin)
            print(len(SKINS_LIST))
        print("Logging finished.")
    else:
        print(
            """
    List is empty, select the correct option to scrape for skins first.
            """
        )
