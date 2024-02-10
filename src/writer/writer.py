"""
    Skins list writing module.
"""

from skin import SKINS_LIST
import json

BASE_FILE_PATH = "scrapedfiles/"
base_dict = list()


def fill_base_dict() -> None:
    for skin in SKINS_LIST:
        skin_dict = {
            "skinName": skin.name,
            "askQty": skin.ask_quantity,
            "askPrice": f"RMB {skin.ask_price}",
            "bidQty": skin.bid_quantity,
            "bidPrice": f"RMB {skin.bid_price}",
            "priceDiff": f"RMB {skin.price_diff}",
            "pctDiff": f"{skin.pct_diff}%",
            "steamPct": f"{skin.steam_pct}%",
            "wear": skin.wear,
            "url": skin.url,
        }
        base_dict.append(skin_dict)


def write(file_name: str) -> None:
    if len(SKINS_LIST) > 0:
        fill_base_dict()
        with open(
            BASE_FILE_PATH + file_name + ".json", "w"
        ) as f:
            json.dump(base_dict, f, indent=2)
            print("Writing was successfull.")
    else:
        print(
            """
        List is empty, select the correct option to scrape for skins first.
            """
        )
