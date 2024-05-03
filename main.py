#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

from time import sleep

class Simple:
    def __init__(self):
        self.Service = FirefoxService(GeckoDriverManager().install())
        self.Options = webdriver.FirefoxOptions()
        self.Driver  = webdriver.Firefox(service=self.Service, options=self.Options)
        self.Domain  = 'https://www.google.com'

    def init(self):
        try: 
            self.Options.add_argument('--private-window') 
            self.Driver.get(self.Domain)

            sleep(3)
            id_elem = '//*[@id="APjFqb"]'

            elem_search = self.Driver.find_element(By.XPATH, id_elem)
            elem_search.clear()
            elem_search.send_keys("youtube")
            elem_search.send_keys(Keys.ENTER)

        except Exception as e:
            print(e)

if __name__ == '__main__':
    Simple = Simple()
    Simple.init()
