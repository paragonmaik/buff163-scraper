from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys

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


def get_filtered_percentage_arg() -> float:
    if len(sys.argv) > 1:
        return float(sys.argv[1])

    return -100


# def result_logger() -> None:
#     print()


# TODO: add filter by diff percentage, diff price, selling
# quantity
def filter_by_percentage(
    actual_pct: float, filtered_pct: float
) -> bool:
    if actual_pct >= filtered_pct:
        return True
    return False


def search_skins(diff_pct: float) -> None:
    card_csgo = driver.find_element(By.CLASS_NAME, "card_csgo")
    items_list = card_csgo.find_elements(By.TAG_NAME, "li")

    for item in items_list:
        values_list = item.find_elements(By.TAG_NAME, "span")
        # TODO: add safe guard by negating condition
        # and return None
        if len(values_list) < 1:
            return

        price_diff = values_list[-1].text
        price_ask = values_list[-6].text
        price_bid = values_list[-4].text
        if filter_by_percentage(
            float(price_diff[-4:-1]), diff_pct
        ):
            print("Price diff and percentage: ", price_diff)
            print("Ask: ", price_ask)
            print("Bid: ", price_bid)


def main():
    # TODO: rename func and var
    filtered_pct = get_filtered_percentage_arg()
    # print(filtered_pct)
    driver.get(BASE_URL)
    search_skins(filtered_pct)
    while True:
        pass


if __name__ == "__main__":
    main()
