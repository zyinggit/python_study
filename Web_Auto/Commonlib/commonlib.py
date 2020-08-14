from selenium import webdriver
import time
class Common(object):
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
    def open_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
    def close_url(self):
        self.driver.quit()
    def __del__(self):  
        time.sleep(3)
        self.driver.quit()
    def locateElement(self,locate_type,value):
        if locate_type=="id":
            el=self.driver.find_element_by_id(value)
        elif locate_type=="name":
            el=self.driver.find_element_by_name(value)
        elif locate_type=="class_name":
            el=self.driver.find_element_by_class_name(value)
        elif locate_type=="tag_name":
            el=self.driver.find_element_by_tag_name(value)
        elif locate_type=="link_text":
            el=self.driver.findt_element_by_link_text(value)
        elif locate_type=="partial_link_text":
            el=self.driver.find_element_by_partial_link_text(value)
        elif locate_type=="xpath":
            el=self.driver.find_element_by_xpath(value)
        elif locate_type=="css":
            el=self.driver.find_element_by_css_selector(value)
        if el is not None:
            return el
    def click(self,locate_type,value):
        el=self.locateElement(locate_type,value)
        el.click()
    def input_data(self,locate_type,value,data):
        el=self.locateElement(locate_type,value)
        el.send_keys(data)
    def get_text(self,locate_type,value):
        el=self.locateElement(locate_type,value)
        return el.text
    def get_attr(self,locate_type,value,data):
        el=self.locateElement(locate_type,value)
        el.get_attribute(data)
if __name__=="__main__":
    com=Common()
    com.open_url("http://www.baidu.com")
    com.click("id","kw")
    com.input_data("id","kw","selenium")
    com.click("id","su")
    time.sleep(3)
    