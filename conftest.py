from fixture.application import Application # import of help class
import pytest
# les10

@pytest.fixture(scope = 'session') #fixture created for whole session  # inicialize fixture for pytest
def app(request):
    fixture = Application() # fixture uses __init__ from application.py
    fixture.session.login(username="Admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
