import os

import pytest

from hello_cloud_security.app import get_environment, greet


def test_greet_returns_string():
    assert isinstance(greet(), str)


def test_greet_contains_env():
    result = greet()
    assert "env=" in result


def test_get_environment_default():
    os.environ.pop("APP_ENV", None)
    assert get_environment() == "local"


def test_get_environment_custom(monkeypatch):
    monkeypatch.setenv("APP_ENV", "staging")
    assert get_environment() == "staging"
