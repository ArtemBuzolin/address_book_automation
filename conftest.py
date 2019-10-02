from fixture.application import Application # import of help class
import pytest
# les10

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application() # fixture uses __init__ from application.py

    else:
        if fixture.is_valid() is False:
            fixture = Application()  # fixture uses __init__ from application.py
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope = 'session', autouse=True) #fixture created for whole session  # inicialize fixture for pytest
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
