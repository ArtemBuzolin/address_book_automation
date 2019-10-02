from model.group_params import GroupParams
from time import sleep

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(GroupParams(name = 'nnn', header = 'www', footer= 'sss'))
    app.group.delete_first_group()
