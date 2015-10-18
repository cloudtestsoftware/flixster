from flixster.qa.pages.abstract     import FlixsterQAPage
from selenium.webdriver.support.ui  import Select
from selenium.webdriver.common.keys import Keys
import time, datetime


class pg_Demo (FlixsterQAPage):
    
    def initLocators(self):           # ====== Locators: ======= #
        self.lnk_Change     = "xpath=//div[2]/div/div/form/div[3]/a"
        self.txt_address    = "id=showtimes-finder-location-input"        
        self.btn_Save       = "id=showtimes-finder-save-location-btn"
        self.lnk_Thtr       = "xpath=//div[2]/div[2]/div/div/div/div/a/div"
        self.lbl_Name       = "xpath=//strong[contains(., 'Century Redwood City 20')]"
        self.lbl_Address    = "xpath=//span[contains(., 'Redwood City, California')]"

    def goto_Login_page (self, url) : # ====== Functions: ====== # 
        self.driver.get(url + "/login")
        time.sleep(1)
        
    def do_LogIn (self, name, password) : 
        self.get_element("id=authLogin").send_keys (name)
        self.get_element("name=authPass").send_keys (password)
        self.get_element("css=button.btn.primary").click ()
        time.sleep(1)
        
    def do_click_Change_Location_link (self) : # ====== Functions: ====== #
        self.get_element(self.lnk_Change).click ()
        time.sleep(1)