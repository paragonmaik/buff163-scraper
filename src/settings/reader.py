"""
    Settings reading module.
"""

import json

from typing import Any


class Options:
    def __init__(
        self,
        price_diff: float,
        pct_diff: float,
        ask_qty: int,
        bid_qty: int,
        wear: str,
        page_limit: int,
    ) -> None:
        self.price_diff = price_diff
        self.pct_diff = pct_diff
        self.ask_qty = ask_qty
        self.bid_qty = bid_qty
        self.wear = wear
        self.page_limit = page_limit

    price_diff: float = 0
    pct_diff: float = 0
    ask_qty: int = 0
    bid_qty: int = 0
    wear: str = ""
    page_limit: int = 0

    def __str__(self) -> str:
        return f"""
        Price difference: {self.price_diff}
        Percentage difference: {self.pct_diff}
        Ask quantity: {self.ask_qty}
        Bid quantity: {self.bid_qty}
        Wear: {self.wear}
        Page limit: {self.page_limit}
                """


OPTIONS: Options = Options(0, 0, 0, 0, "", 0)


def handle_settings() -> None:
    print("Please enter the path to config file:")
    path_to_url = input()
    read_json_settings(path_to_url)


def convert_file_to_var(data: Any) -> None:
    try:
        OPTIONS.price_diff = data["priceDiff"]
        OPTIONS.pct_diff = data["pctDiff"]
        OPTIONS.ask_qty = data["askQty"]
        OPTIONS.bid_qty = data["bidQty"]
        OPTIONS.wear = data["wear"]
        OPTIONS.page_limit = data["pageLimit"]

        print("Settings were successfully loaded.")
    except Exception as e:
        print(f"Unable to load settings: {e}")
        raise e


def read_json_settings(path: str) -> None:
    with open(path, "r") as f:
        data = json.load(f)
        convert_file_to_var(data)
    f.close()


def read_settings_on_bot_load(path: str) -> None:
    print("Loading settings.json located at root folder...")
    read_json_settings(path)
