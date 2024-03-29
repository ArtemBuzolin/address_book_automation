from model.group_params import GroupParams
from time import sleep
from random import randrange

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(GroupParams(name = 'nnn', header = 'www', footer= 'sss'))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    del old_groups[0:1]
    assert old_groups  == new_groups


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(GroupParams(name = 'nnn', header = 'www', footer= 'sss'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    del old_groups[index:index+1]
    assert old_groups  == new_groups

