"""
    Skin Class {5+5}
"""

from typing import List


class Skin:
    def __init__(
        self,
        name: str | None,
        url: str | None,
        ask_quantity: int,
        ask_price: float,
        bid_quantity: int,
        bid_price: float,
        price_diff: float,
        pct_diff: float,
        steam_pct: float,
        wear: str,
    ) -> None:
        self.name = name or ""
        self.url = url or ""
        self.ask_quantity = ask_quantity
        self.ask_price = ask_price
        self.bid_quantity = bid_quantity
        self.bid_price = bid_price
        self.price_diff = price_diff
        self.pct_diff = pct_diff
        self.steam_pct = steam_pct
        self.wear = wear

    name: str = ""
    url: str = ""
    ask_quantity: int = 0
    ask_price: float = 0
    bid_quantity: int = 0
    bid_price: float = 0
    price_diff: float = 0
    pct_diff: float = 0
    steam_pct: float = 0
    wear: str = ""

    def __str__(self) -> str:
        return f"""
    Name: {self.name.split("(", 1)[0]}
    Ask Quantity: {self.ask_quantity}
    Ask Price: ¥ {self.ask_price}
    Bid Quantity: {self.bid_quantity}
    Bid Price: ¥ {self.bid_price}
    Price Difference: ¥ {self.price_diff}
    Percentage Difference: {self.pct_diff}%
    Steam percentage: {self.steam_pct}%
    Wear: {self.wear}
    URL: {self.url.split("(", 1)[0]}
        """


SKINS_LIST: List[Skin] = list()
