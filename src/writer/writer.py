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
            "askPrice": f"¥ {skin.ask_price}",
            "bidQty": skin.bid_price,
            "bidPrice": f"¥ {skin.bid_price}",
            "priceDiff": f"¥ {skin.price_diff}",
            "pctDiff": f"{skin.pct_diff}%",
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
    else:
        print(
            """
        List is empty, select the correct option to scrape for skins first.
            """
        )
