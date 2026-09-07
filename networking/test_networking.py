import pytest
from port_scanner import check_port
from ping_test import ping_host


def test_google_is_reachable():
    assert ping_host("google.com") is True


def test_https_port_open_on_google():
    assert check_port("google.com", 443) is True


def test_closed_port_on_localhost():
    assert check_port("127.0.0.1", 9999) is False
