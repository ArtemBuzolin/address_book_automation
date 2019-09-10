from model.group_params import GroupParams
from time import sleep
sleep(4)
def test_modify_group_name(app):
    wd = app.wd
    app.session.login(username="Admin", password="secret")
    app.group.modify_firstgroup(GroupParams(name='New group'))
    app.session.logout()
sleep(4)

def test_modify_group_header(app):
    wd = app.wd
    app.session.login(username="Admin", password="secret")
    app.group.modify_firstgroup(GroupParams(header='New Header'))
    app.session.logout()