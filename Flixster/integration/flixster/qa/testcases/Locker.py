from flixster.qa.testcases.abstract         import FlixsterQATestCase
from selenium.webdriver.common.by           import By
from flixster.qa.pages.pg_Demo              import pg_Demo

import time, datetime


class Locker(FlixsterQATestCase):

    def loadPages(self):
        self.pg_Demo=pg_Demo(self)


    def test_Verify_Theater_showtimes (self) : 
        ''' ****************************************************************************************************************
        Description: Test case verifies that theater showtimes are being returned by API.
        
        Test Case Steps:
        # Navigate to Home page
        # Log in with existing Flixster user
        # Click on In Theaters link
        # Get and store name of the first movie of Now playing section
        # Click on Get showtimes link for the first movie
        # Enter zip code into Zip code file and click Go button
        # Verify that the top theater name is being dispalyed
        # Verify that the top theater address is being dispalyed
        # Verify that the top theater phone number is being dispalyed
        *****************************************************************************************************************'''

        # Navigate to Home page
        self.pg_Demo.goto_url(self.base_url + self.url_path)
        self.pg_Demo.goto_Login_page(self.base_url + self.url_path)

        # Log in with existing Flixster user
        self.pg_Demo.do_LogIn ("test_demo@aol.com", "password")

        # Click on the first movie of Now playing section
        self.pg_Demo.get_element(self.pg_Demo.lnk_Thtr).click()
        time.sleep(3)

        # Click on change location link
        self.pg_Demo.do_click_Change_Location_link()
        time.sleep(1)
        
        # Enter zip code into Zip code file and click Go button
        self.pg_Demo.get_element(self.pg_Demo.txt_address).send_keys("94404")
        time.sleep(1)
        self.pg_Demo.get_element(self.pg_Demo.btn_Save).click()
        time.sleep(5)
        
        # Verify that the top theater name is being dispalyed
        self.pg_Demo.verifyElementExists(self.pg_Demo.lbl_Name)

        # Verify that the top theater address is being dispalyed
        self.pg_Demo.verifyElementExists(self.pg_Demo.lbl_Address)
    # end of the test. -----------------------------------------------------------------------------------------------------
