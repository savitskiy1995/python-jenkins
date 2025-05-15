# -*- coding: utf-8 -*-
import pytest
from application import Application
from group import Group

# Добавьте в начало файлов (после импортов) следующую строку:
pytestmark = pytest.mark.html

@pytest.fixture
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="new_group", header="logo"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header=""))
    app.logout()
