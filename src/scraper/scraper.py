"""
    Scraper module.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from skin import Skin, SKINS_LIST

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


def filter_by_float_value(
    actual: float, filtered: float
) -> bool:
    if actual >= filtered:
        return True
    return False


def result_logger() -> None:
    for skin in SKINS_LIST:
        print(skin)


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
        price_ask = values_list[-6].text.split("ask", 1)[0][1:]
        price_bid = values_list[-4].text.split("bid", 1)[0][1:]
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
        skin = Skin(
            skin_name,
            skin_url,
            int(ask_quantity),
            float(price_ask),
            int(bid_quantity),
            float(price_bid),
            float(price_diff),
            float(pct_diff),
            skin_wear,
        )
        SKINS_LIST.append(skin)
        result_logger()
    print(count)
