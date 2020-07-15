from Settings1 import wd,url2
from selenium.webdriver.common.by import By


class fkartLogin():
    def wbget1(self):
        wd.get(url2)
        wd.maximize_window()
        pageTitle = wd.title
        handles=wd.window_handles
        print("handles are",handles)
        for i in handles:
            wd.switch_to.window(i)
            handle_title=wd.title
            if handle_title!=pageTitle:
                wd.switch_to.window(i)
                break


       #wd.find_element_by_xpath("//input[@class='_2zrpKA _2rqcw- _2VUCMV F_Atl2 _1dBPDZ']").sendkeys("email or mobilenumber")
       #wd.find_elements_by_xpath("//input[@class='_2zrpKA _2rqcw- _3v41xv _1dBPDZ']").sendkeys("")
        wd.find_element_by_xpath('//div[@class="_39M2dM JB4AMj"]/input[@type="text"]').send_keys('9591071147')
        wd.find_element_by_xpath("//input[@type='password']").send_keys('rajath8127')
        wd.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']").click()
        print("Logging in Please wait")


obj=fkartLogin()
obj.wbget1()