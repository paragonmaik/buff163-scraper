"""
    Scraper module.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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


# variables
BASE_URL = "https://buff.163.com/market/csgo"
# ABSOLUTE_PATH_UNPACKED = '/home/maik/Dev/BuffUtility'
ABSOLUTE_PATH_PACKED = (
    "/home/maik/Dev/cs-automaton/src/extensions/BuffUtility.crx"
)

service = Service()
options = webdriver.ChromeOptions()
options.add_extension(ABSOLUTE_PATH_PACKED)
driver = webdriver.Chrome(service=service, options=options)


# TODO: add func to concatenate skins into a list that
# can be logged and written into file
# def add_skins_to_list()


# TODO: use the same func for all comparisons with the same
# signature
def filter_by_float_value(
    actual: float, filtered: float
) -> bool:
    if actual >= filtered:
        return True
    return False


def filter_by_percentage(
    actual_pct: float, filtered_pct: float
) -> bool:
    if actual_pct >= filtered_pct:
        return True
    return False


def filter_by_price(
    actual_price: float, filtered_price: float
) -> bool:
    if actual_price >= filtered_price:
        return True
    return False


def filter_by_quantity(
    actual_quantity: float, filtered_quantity: float
) -> bool:
    if actual_quantity >= filtered_quantity:
        return True
    return False


def search_skins(
    diff_pct: float,
    diff_price: float,
    min_ask: float,
    min_bid: float,
) -> None:
    driver.get(BASE_URL)

    card_csgo = driver.find_element(By.CLASS_NAME, "card_csgo")
    items_list = card_csgo.find_elements(By.TAG_NAME, "li")
    count = 0

    for item in items_list:
        values_list = item.find_elements(By.TAG_NAME, "span")
        if len(values_list) < 1:
            return

        price_diff = values_list[-1].text
        price_ask = values_list[-6].text
        price_bid = values_list[-4].text
        skin_wear = values_list[-7].text
        ask_quantity = values_list[-6].text.split("(", 1)[-1][
            :-1
        ]
        bid_quantity = values_list[-4].text.split("(", 1)[-1][
            :-1
        ]

        if not filter_by_float_value(
            float(price_diff[-5:-1]), diff_pct
        ):
            continue

        if not filter_by_float_value(
            float(price_diff.split("|", 1)[0][1:]), diff_price
        ):
            continue

        if not filter_by_float_value(
            float(ask_quantity), min_ask
        ):
            continue

        if not filter_by_float_value(
            float(bid_quantity), min_bid
        ):
            continue

        count += 1
        print("Price diff and percentage: ", price_diff)
        print("Ask: ", price_ask)
        print("Bid: ", price_bid)
        print("Ask quantity: ", ask_quantity)
        print("Bid quantity: ", bid_quantity)
        print("Skin wear: ", skin_wear)
        print("Diff with: ", price_diff.split("|", 1)[0][1:])
    print(count)
