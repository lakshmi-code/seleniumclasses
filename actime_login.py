from Settings1 import wd,url1
from selenium.webdriver.common.by import By

class actimelog():
    def navigate(self):
        wd.get(url1)
        wd.find_element_by_name("username").send_keys("admin")
        wd.implicitly_wait(2)
        wd.find_element_by_name("pwd").send_keys("manager")



obj=actimelog()
obj.navigate()

