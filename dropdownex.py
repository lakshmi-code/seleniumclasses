from Settings1 import wd,url3
from selenium.webdriver.common.by import By

class dropd():
    def ex1(self):
        wd.get(path)#of the html
        element=wd.find_element_by_id("cars")
        s_obj=select(element)
        s_obj.select_by_value("sub1")
        s_obj.select_by_index(3)
        s_obj.select_by_visible_text("Mysore")
        value=s_obj.first_selected_option
        print("first option",value.text)
        options=s_obj.all_selected_options
        for i in options:
            print("options are ")
            print(i.text)


obj=dropd()
obj.ex1()
