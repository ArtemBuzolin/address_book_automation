from time import sleep
from model.group_params import GroupParams
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        # open groups page]
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click()


    def return_to_groups_page(self):
        # return to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, GroupParams):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        self.fill_group_form(GroupParams)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, GroupParams):
        wd = self.app.wd
        self.change_field_value("group_name", GroupParams.name)
        self.change_field_value("group_header", GroupParams.header)
        self.change_field_value("group_footer", GroupParams.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name('delete').click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_firstgroup(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open group
        wd.find_element_by_name('edit').click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit
        wd.find_element_by_name('update').click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name('selected[]'))

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_group_page()
        for i in wd.find_elements_by_name('selected[]'):
            i.click()
        wd.find_element_by_name('delete').click()
        self.return_to_groups_page()
        self.group_cache = None

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(GroupParams(name = text , id = id))

        return list(self.group_cache)



