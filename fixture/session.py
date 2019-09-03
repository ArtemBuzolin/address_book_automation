class SessionHelper:

    def __init__(self, app):
        """parameter app comes from self in SessionHelper(self)
        and include inside webdriver as wd and all methods (from application.py) """
        self.app = app

    def login(self, username, password):
        # login
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def logout(self):
        # logout
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
