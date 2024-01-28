from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from commands.reader import read_flags, USED_COMMANDS_LIST


# variables
BASE_URL = "https://buff.163.com/market/csgo"
# ABSOLUTE_PATH_UNPACKED = '/home/maik/Dev/BuffUtility'
ABSOLUTE_PATH_PACKED = (
    "/home/maik/Dev/cs-automaton/src/extensions/BuffUtility.crx"
)

# Initial Setup
service = Service()
options = webdriver.ChromeOptions()

options.add_extension(ABSOLUTE_PATH_PACKED)

driver = webdriver.Chrome(service=service, options=options)


def get_float_type_command(flag: str) -> float:
    if flag in USED_COMMANDS_LIST:
        return float(USED_COMMANDS_LIST[flag])
    return -100


def result_logger(skins_list: List[WebElement]) -> None:
    price_diff = skins_list[-1].text
    price_ask = skins_list[-6].text
    price_bid = skins_list[-4].text

    print("Price diff and percentage: ", price_diff)
    print("Ask: ", price_ask)
    print("Bid: ", price_bid)


# TODO: use the same func for all comparisons with the same
# signature
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
    card_csgo = driver.find_element(By.CLASS_NAME, "card_csgo")
    items_list = card_csgo.find_elements(By.TAG_NAME, "li")

    for item in items_list:
        values_list = item.find_elements(By.TAG_NAME, "span")
        if len(values_list) < 1:
            return

        price_diff = values_list[-1].text
        price_ask = values_list[-6].text
        price_bid = values_list[-4].text
        ask_quantity = price_ask.split("(", 1)[-1][:-1]
        bid_quantity = price_bid.split("(", 1)[-1][:-1]

        if not filter_by_percentage(
            float(price_diff[-4:-1]), diff_pct
        ):
            continue

        if not filter_by_price(
            float(price_diff[-11:-7]), diff_price
        ):
            continue

        if not filter_by_quantity(float(ask_quantity), min_ask):
            continue

        if not filter_by_quantity(float(bid_quantity), min_bid):
            continue

        print("Price diff and percentage: ", price_diff)
        print("Ask: ", price_ask)
        print("Bid: ", price_bid)
        print("Ask quantity: ", ask_quantity)
        print("Bid quantity: ", bid_quantity)


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
    driver.get(BASE_URL)

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
