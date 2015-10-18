from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


class FlixsterQAPage():
    def __init__(self, testcase, url_path=""):
        self.testcase=testcase
        self.driver=testcase.driver
        self.url_base=testcase.base_url
        self.url_path=url_path
        
        self.initLocators()
        
    def goto_url(self, custom_url=None):
        if(custom_url == None):
            self.driver.get(self.url_base + self.url_path)
        else:
            self.driver.get(custom_url)
        time.sleep(1)
        
    def get_element(self,  full_locator, waitTime=10, errorMessage = "Element not found!") :
        if isinstance(full_locator, list):
            locator_type = full_locator[1].lower()
            if (locator_type == "id" or locator_type == "class" or locator_type == "class_name" or locator_type == "css" or locator_type == "css_selector" \
                or locator_type == "link" or locator_type == "link_text" or locator_type == "p_link" or locator_type == "partial_link_text" or locator_type == "name" \
                or locator_type == "tag" or locator_type == "tag_name" or locator_type == "xpath") :
                locator = full_locator[0]
            else :
                raise AssertionError("ERROR from <get_element>: wrong type of Full Locator as LIST !!!")
                
        elif isinstance(full_locator, str):
            splited_locator = full_locator.split("=", 1)
            locator_type = splited_locator[0].lower()
            if (locator_type == "id" or locator_type == "class" or locator_type == "class_name" or locator_type == "css" or locator_type == "css_selector" \
                or locator_type == "link" or locator_type == "link_text" or locator_type == "p_link" or locator_type == "partial_link_text" or locator_type == "name" \
                or locator_type == "tag" or locator_type == "tag_name" or locator_type == "xpath") :
                locator = splited_locator[1]
            else :
                raise AssertionError("ERROR from <get_element>: wrong type of Full Locator as STRING !!!")
        else:
            raise AssertionError("ERROR from <get_element>: <full_locator> is not List or String!")

        if locator_type == "id" :
            by=By.ID
        elif locator_type == "class" or locator_type == "class_name" :
            by=By.CLASS_NAME
        elif locator_type == "css"or locator_type == "css_selector" :
            by=By.CSS_SELECTOR
        elif locator_type == "link" or locator_type == "link_text" :
            by=By.LINK_TEXT
        elif locator_type == "p_link" or locator_type == "partial_link_text" :
            by=By.PARTIAL_LINK_TEXT
        elif locator_type == "name" :
            by=By.NAME
        elif locator_type == "tag" or locator_type == "tag_name" :
            by=By.TAG_NAME
        elif locator_type == "xpath" :
            by=By.XPATH
        
        try:
            return WebDriverWait(self.driver, waitTime).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            raise AssertionError(errorMessage + " locator:" + str(full_locator))
            
    def verifyElementExists (self, full_locator, errorMessage="Element does NOT exist!"):
        self.get_element(full_locator,0)