def delete_first_group(app):
    wd = app.wd
    app.session.login(username="Admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()