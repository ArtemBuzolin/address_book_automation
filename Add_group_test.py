# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.wd = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True



    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_group_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, gname, header, footer):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(gname)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        self.login(wd, username="Admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, gname="111", header="22222222", footer="222")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        self.login(wd, username="Admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, gname="", header="", footer="")
        self.return_to_groups_page(wd)
        self.logout(wd)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
