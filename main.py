#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

from time import sleep

def main():
    try:
        service_ = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument('--private-window')
        driver = webdriver.Firefox(service=service_, options=options)

        domain = "https://www.google.com"
    
        driver.get(domain)

        sleep(3)
        input_search = '//*[@id="APjFqb"]'

        elem = driver.find_element(By.XPATH, input_search)
        elem.clear()
        elem.send_keys("youtube")
        elem.send_keys(Keys.ENTER)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
