from model.group_params import GroupParams
from time import sleep
def test_modify_group_name(app):
    app.group.modify_firstgroup(GroupParams(name='New group'))

def test_modify_group_header(app):
    app.group.modify_firstgroup(GroupParams(header='New Header'))
