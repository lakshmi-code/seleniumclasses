from Settings1 import wd,url2
from selenium.webdriver.common.by import By


class xpathLogin():
    def wbget1(self):
        wd.get(url2)
        wd.find_element_by_xpath("//input[@class='_2zrpKA _2rqcw- _2VUCMV F_Atl2 _1dBPDZ']").sendkeys("email or mobilenumber")
        wd.find_elements_by_xpath("//input[@class='_2zrpKA _2rqcw- _3v41xv _1dBPDZ']")
        wd.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']").click()
        print("Logging in Please wait")


obj=xpathLogin()
obj.wbget1()