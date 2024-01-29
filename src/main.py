from selenium.webdriver.remote.webelement import WebElement
from typing import List
from commands.reader import read_flags, USED_COMMANDS_LIST
from scraper.scraper import search_skins

# variables
BASE_URL = "https://buff.163.com/market/csgo"
# ABSOLUTE_PATH_UNPACKED = '/home/maik/Dev/BuffUtility'
ABSOLUTE_PATH_PACKED = (
    "/home/maik/Dev/cs-automaton/src/extensions/BuffUtility.crx"
)


class Skin:
    def __init__(
        self, name, url, wear, ask, bid, price_diff, pct_diff
    ) -> None:
        self.name = name
        self.url = url
        self.wear = wear
        self.ask = ask
        self.bid = bid
        self.price_diff = price_diff
        self.pct_diff = pct_diff

    name: str = ""
    url: str = ""
    wear: str = ""
    ask: str = ""
    bid: str = ""
    price_diff: float = 0
    pct_diff: float = 0


def get_float_type_command(flag: str) -> float:
    if flag in USED_COMMANDS_LIST:
        return float(USED_COMMANDS_LIST[flag])
    return 0


def result_logger(skins_list: List[WebElement]) -> None:
    price_diff = skins_list[-1].text
    price_ask = skins_list[-6].text
    price_bid = skins_list[-4].text

    print("Price diff and percentage: ", price_diff)
    print("Ask: ", price_ask)
    print("Bid: ", price_bid)


def main():
    read_flags()

    filtered_pct = get_float_type_command("-p")
    filtered_price_diff = get_float_type_command("-v")
    filtered_ask = get_float_type_command("-q")
    filtered_bid = get_float_type_command("-b")
    print(
        filtered_pct,
        filtered_price_diff,
        filtered_ask,
        filtered_bid,
    )
    # driver.get(BASE_URL)

    search_skins(
        filtered_pct,
        filtered_price_diff,
        filtered_ask,
        filtered_bid,
    )
    while True:
        pass


if __name__ == "__main__":
    main()
