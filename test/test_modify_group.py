from model.group_params import GroupParams
def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = GroupParams(name='New group')
    group.id = old_groups[0].id
    app.group.modify_firstgroup(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=GroupParams.id_or_max) == sorted(new_groups, key=GroupParams.id_or_max)

def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_firstgroup(GroupParams(header='New Header'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
