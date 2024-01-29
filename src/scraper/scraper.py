"""
    Scraper module.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import List


class Skin:
    def __init__(
        self,
        name: str | None,
        url: str | None,
        ask_quantity: float,
        ask_price: float,
        bid_quantity: float,
        bid_price: float,
        price_diff: float,
        pct_diff: float,
        wear: str,
    ) -> None:
        self.name = name
        self.url = url
        self.ask_quantity = ask_quantity
        self.ask_price = ask_price
        self.bid_quantity = bid_quantity
        self.bid_price = bid_price
        self.price_diff = price_diff
        self.pct_diff = pct_diff
        self.wear = wear

    name: str | None = ""
    url: str | None = ""
    ask_quantity: float = 0
    ask_price: float = 0
    bid_quantity: float = 0
    bid_price: float = 0
    price_diff: float = 0
    pct_diff: float = 0
    wear: str = ""

    def __str__(self) -> str:
        return ""


# variables
# TODO: add as env variables
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


# def result_logger(skins_list: List[WebElement]) -> None:


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
        url_element = item.find_element(By.TAG_NAME, "a")

        if len(values_list) < 1:
            return

        price_pct_diff = values_list[-1].text
        pct_diff = price_pct_diff[-5:-1]
        price_diff = price_pct_diff.split("|", 1)[0][1:]
        price_ask = values_list[-6].text
        price_bid = values_list[-4].text
        skin_wear = values_list[-7].text
        ask_quantity = values_list[-6].text.split("(", 1)[-1][
            :-1
        ]
        bid_quantity = values_list[-4].text.split("(", 1)[-1][
            :-1
        ]
        skin_name = url_element.get_attribute("title")
        skin_url = url_element.get_attribute("href")

        if not filter_by_float_value(
            float(price_pct_diff[-5:-1]), diff_pct
        ):
            continue

        if not filter_by_float_value(
            float(price_pct_diff.split("|", 1)[0][1:]),
            diff_price,
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
        print("Name: ", skin_name)
        print("Skin wear: ", skin_wear)
        print(
            "Price diff and percentage: ",
            price_diff,
            "|",
            pct_diff,
        )
        print("Ask price: ", price_ask)
        print("Ask quantity: ", ask_quantity)
        print("Bid price: ", price_bid)
        print("Bid quantity: ", bid_quantity)
        print("URL: ", skin_url)
        skin = Skin(
            skin_name,
            skin_url,
            float(price_ask),
            float(ask_quantity),
            float(price_bid),
            float(bid_quantity),
            float(price_diff),
            float(pct_diff),
            skin_wear,
        )
    print(count)
