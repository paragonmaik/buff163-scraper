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


def filter_percentage(
    actual_pct: float, filtered_pct: float
) -> None:
    actual_pct = filtered_pct


def search_skins() -> None:
    driver.get(BASE_URL)
    card_csgo = driver.find_element(By.CLASS_NAME, "card_csgo")
    items_list = card_csgo.find_elements(By.TAG_NAME, "li")

    for item in items_list:
        values_list = item.find_elements(By.TAG_NAME, "span")
        if len(values_list) > 0:
            print(values_list[-1].text, sys.argv[1])


def main():
    search_skins()
    while True:
        pass


if __name__ == "__main__":
    main()
