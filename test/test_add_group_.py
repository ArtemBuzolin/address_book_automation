# -*- coding: utf-8 -*-]
from time import sleep

from model.group_params import GroupParams


"""
fixture transfered to conftest.py 

from fixture.application import Application # import of help class
import pytest

@pytest.fixture   # inicialize fixture for pytest
def app(request):
    fixture = Application() # fixture uses __init__ from application.py
    request.addfinalizer(fixture.destroy)
    return fixture
"""



def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = GroupParams(name="111", header="22222222", footer="222")
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    app.session.logout()
    old_groups.append(group)
    assert sorted(old_groups, key = GroupParams.id_or_max) == sorted(new_groups, key = GroupParams.id_or_max)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = GroupParams(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=GroupParams.id_or_max) == sorted(new_groups, key=GroupParams.id_or_max)



