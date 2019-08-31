# -*- coding: utf-8 -*-
from application import Application # import of help class
import pytest

from group import Group


@pytest.fixture   # inicialize fixture for pytest
def app(request):
    fixture = Application() # fixture uses __init__ from application.py
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    wd = app.wd
    app.login(username="Admin", password="secret")
    app.create_group(Group(name="111", header="22222222", footer="222"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="Admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

    def tearDown(self):
        self.app.destroy()
