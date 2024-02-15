"""
    Scraper module.
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from skin import Skin, SKINS_LIST
from settings.reader import OPTIONS
import time


def filter_by_float_value(
    actual: float, filtered: float
) -> bool:
    if actual >= filtered:
        return True
    return False


def scrape(driver: WebDriver, url: str) -> None:
    driver.get(url)
    current_page = 1
    page_limit = OPTIONS.page_limit
    time.sleep(15)
    print("Please, set the necessary filters.")
    while current_page <= page_limit:
        time.sleep(10)
        search_skins(
            OPTIONS.pct_diff,
            OPTIONS.price_diff,
            OPTIONS.ask_qty,
            OPTIONS.bid_qty,
            driver,
        )
        time.sleep(15)
        paginate(driver)
        current_page += 1
    print("Scraping finished")
    return


def paginate(driver: WebDriver) -> None:
    pagination_div = (
        driver.find_element(By.CLASS_NAME, "simple-pagination")
        .find_element(By.TAG_NAME, "ul")
        .find_elements(By.TAG_NAME, "li")
    )
    pagination_div[-1].click()


def handle_find_element(
    item: WebElement, class_name: str
) -> str | None:
    pct_price = None
    try:
        pct_price = item.find_element(
            By.CLASS_NAME, class_name
        ).text
    except NoSuchElementException:
        pass

    return pct_price


def search_skins(
    diff_pct: float,
    diff_price: float,
    min_ask: float,
    min_bid: float,
    driver: WebDriver,
) -> None:
    card_csgo = driver.find_element(By.CLASS_NAME, "card_csgo")
    items_list = card_csgo.find_elements(By.TAG_NAME, "li")

    for item in items_list:
        values_list = item.find_elements(By.TAG_NAME, "span")
        url_element = item.find_element(By.TAG_NAME, "a")

        if len(values_list) < 1:
            return

        skin_wear = handle_find_element(item, "tag") or ""
        price_pct_diff = (
            handle_find_element(item, "pct-diff") or ""
        )
        pct_diff = price_pct_diff.split("|", 1)[1][:-1]
        price_diff = price_pct_diff.split("|", 1)[0][1:]

        steam_pct_element = (
            handle_find_element(item, "pct-steam") or ""
        )
        steam_pct = steam_pct_element[1:-1]
        ask_element = handle_find_element(item, "ask-span") or ""
        bid_element = handle_find_element(item, "bid-span") or ""

        ask_quantity = ask_element.split("(", 1)[-1][:-1]
        price_ask = ask_element.split("ask", 1)[0][1:]

        price_bid = bid_element.split("bid", 1)[0][1:]
        bid_quantity = bid_element.split("(", 1)[-1][:-1]

        skin_name = url_element.get_attribute("title")
        skin_url = url_element.get_attribute("href")

        try:
            if not filter_by_float_value(
                float(pct_diff), diff_pct
            ):
                continue
        except Exception as e:
            pct_diff = 0
            print(e)

        try:
            if not filter_by_float_value(
                float(price_diff),
                diff_price,
            ):
                continue
        except Exception as e:
            price_diff = 0
            print(e)

        try:
            if not filter_by_float_value(
                float(ask_quantity), min_ask
            ):
                continue
        except Exception as e:
            ask_quantity = 0
            print(e)

        try:
            if not filter_by_float_value(
                float(bid_quantity), min_bid
            ):
                continue
        except Exception as e:
            bid_quantity = 0
            print(e)

        skin = Skin(
            skin_name,
            skin_url,
            int(ask_quantity),
            float(price_ask),
            int(bid_quantity),
            float(price_bid),
            float(price_diff),
            float(pct_diff),
            float(steam_pct),
            skin_wear,
        )
        SKINS_LIST.append(skin)
