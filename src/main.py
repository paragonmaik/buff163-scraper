from commands.reader import read_flags, get_float_type_command
from scraper.scraper import search_skins
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from signin.signin import manual_buff_login


BUFF_MARKET_URL = "https://buff.163.com/market/csgo"
BUFF_BASE_URL = "https://buff.163.com/"
# ABSOLUTE_PATH_UNPACKED = '/home/maik/Dev/BuffUtility'
ABSOLUTE_PATH_PACKED = (
    "/home/maik/Dev/cs-automaton/src/extensions/BuffUtility.crx"
)
service = Service()
options = webdriver.ChromeOptions()
options.add_extension(ABSOLUTE_PATH_PACKED)
driver = webdriver.Chrome(service=service, options=options)


def main():
    read_flags()
    driver.get(BUFF_BASE_URL)
    manual_buff_login()
    driver.get(BUFF_MARKET_URL)

    search_skins(
        get_float_type_command("-p"),
        get_float_type_command("-v"),
        get_float_type_command("-q"),
        get_float_type_command("-b"),
        driver,
    )
    while True:
        pass


if __name__ == "__main__":
    main()
