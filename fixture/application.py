from selenium import webdriver
from fixture.session import SessionHelper
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self) # connection with class from session.py, with parameter self( for using self.wd(webdriver(__init__)) )

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")



    def open_group_page(self):
        # open groups page
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, Group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        # return to groups page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()



    def destroy(self):
        self.wd.quit()