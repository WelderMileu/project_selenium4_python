#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

from time import sleep

class Simple:
    def __init__(self):
        self.service = FirefoxService(GeckoDriverManager().install())
        self.options = webdriver.FirefoxOptions()
        self.private = self.options.add_argument('--private-window')
        self.driver  = webdriver.Firefox(service=self.service, options=self.options)
        self.domain  = ''

    def init(self):
        try: 
            self.domain = 'https://www.google.com'
            self.driver.get(self.domain)

            sleep(3)
            id_elem = '//*[@id="APjFqb"]'

            elem_search = self.driver.find_element(By.XPATH, id_elem)
            elem_search.clear()
            elem_search.send_keys("youtube")
            elem_search.send_keys(Keys.ENTER)

        except Exception as e:
            print(e)

    def instagram_stories(self):
        try:
            from base64 import b64decode

            path_url    = ""
            prof_hash   = ""
            prof_decode = b64decode(prof_hash).decode()

            self.domain = path_url
            self.driver.get(self.domain)

            xpath = '/html/body/div[1]/header/div[1]/div/form/div/input'
            ipt_search = self.driver.find_element(By.XPATH, xpath)

            ipt_search.send_keys(prof_decode)
            ipt_search.send_keys(Keys.ENTER)

            sleep(3)
            original_tab = self.driver.current_window_handle
            self.driver.switch_to.window(original_tab)

            button_dowload_xpath = '/html/body/div[1]/div[1]/div/div/ul[2]'
            all_button_download  = self.driver.find_element(By.XPATH, button_dowload_xpath)
            
            link = all_button_download.find_elements(By.TAG_NAME, 'a')

            for x in link:
                import wget
                from uuid import uuid4

                url = x.get_attribute('href')
                wget.download(url)

        except Exception as e:
            print(e)

    def main(self):
        Simple.instagram_stories()


if __name__ == '__main__':
    Simple = Simple()
    Simple.main()
