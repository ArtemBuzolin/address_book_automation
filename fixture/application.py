from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self) # connection with class from session.py, with parameter self( for using self.wd(webdriver(__init__)) )
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()