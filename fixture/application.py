from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self) # connection with class from session.py, with parameter self( for using self.wd(webdriver(__init__)) )
        self.group = GroupHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()