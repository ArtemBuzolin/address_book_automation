from model.group_params import GroupParams

def test_delete_all_groups(app):
    if app.group.count() == 0:
        app.group.create(GroupParams(name = 'nnn', header = 'www', footer= 'sss'))
    app.group.delete_all_groups()