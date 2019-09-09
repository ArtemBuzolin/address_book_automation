# -*- coding: utf-8 -*-]


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
    wd = app.wd
    app.session.login(username="Admin", password="secret")
    app.group.create(GroupParams(name="111", header="22222222", footer="222"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.create(GroupParams(name="", header="", footer=""))
    app.session.logout()


