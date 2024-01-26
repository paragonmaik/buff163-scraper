from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BASE_URL = "https://buff.163.com/market/csgo"

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service,options=options)

def search():
    print("Hello Sailor")

def main():
    search()

if __name__ == "__main__":
    main()
