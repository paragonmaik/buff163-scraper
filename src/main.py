from scraper.scraper import scrape
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from logger.logger import log
from settings.reader import (
    handle_settings,
    read_settings_on_bot_load,
    OPTIONS,
)
from writer.writer import write


BUFF_MARKET_URL = "https://buff.163.com/market/csgo"
BUFF_BASE_URL = "https://buff.163.com/"
# ABSOLUTE_PATH_UNPACKED = '/home/maik/Dev/BuffUtility'
ABSOLUTE_PATH_PACKED = (
    "/home/maik/Dev/cs-automaton/extensions/BuffUtility.crx"
)
ABSOLUTE_SETTINGS_PATH = (
    "/home/maik/Dev/cs-automaton/settings.json"
)
service = Service()
options = webdriver.ChromeOptions()
options.add_extension(ABSOLUTE_PATH_PACKED)
driver = webdriver.Chrome(service=service, options=options)


def show_options() -> None:
    print(
        """
    1. Search for skins.
    2. Load settings (Scrape, Buy orders).
    3. Display settings (Scrape, Buy orders).
    4. Display scraped skins.
    5. Write scraped skins to file.
        """
    )


def control_bot_flow() -> None:
    read_settings_on_bot_load(ABSOLUTE_SETTINGS_PATH)
    print("Please sign in...")
    print(
        "After signing in, choose one of the following options:"
    )
    while True:
        show_options()
        user_input = input()
        print(f"You selected option: {user_input}")
        if int(user_input) == 1:
            scrape(driver, BUFF_MARKET_URL)
        if int(user_input) == 2:
            handle_settings()
        if int(user_input) == 3:
            print(OPTIONS)
        if int(user_input) == 4:
            log()
        if int(user_input) == 5:
            write("test")
        else:
            print("Please select a valid option.")


def main():
    driver.get(BUFF_BASE_URL)
    control_bot_flow()
    # log()

    # Guarantees page will stay open
    while True:
        pass


if __name__ == "__main__":
    main()
