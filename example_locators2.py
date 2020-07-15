from Settings1 import wd,url
from selenium.webdriver.common.by import By

class locators:
    def basicloc(self):
        wd.get(url)
        wd.find_element(By.ID)
        wd.find_element(By.LINK_TEXT)
        wd.find_element(By.PARTIAL_LINK_TEXT)
