from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BASE_URL = "https://buff.163.com/market/csgo"
# ABSOLUTE_PATH_UNPACKED = '/home/maik/Dev/BuffUtility'
ABSOLUTE_PATH_PACKED = '/home/maik/Dev/cs-automaton/src/extensions/BuffUtility.crx'

# Initial Setup
service = Service()
options = webdriver.ChromeOptions()

options.add_extension(ABSOLUTE_PATH_PACKED)

driver = webdriver.Chrome(service=service,options=options)

def search():
    driver.get(BASE_URL)
    while(True):
        pass

def main():
    search()

if __name__ == "__main__":
    main()
