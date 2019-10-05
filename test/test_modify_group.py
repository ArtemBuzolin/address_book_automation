from model.group_params import GroupParams
from random import randrange

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(GroupParams(name = 'nnn', header = 'www', footer= 'sss'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = GroupParams(name='New group')
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=GroupParams.id_or_max) == sorted(new_groups, key=GroupParams.id_or_max)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(GroupParams(name = 'nnn', header = 'www', footer= 'sss'))
    old_groups = app.group.get_group_list()
    app.group.modify_firstgroup(GroupParams(header='New Header'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
