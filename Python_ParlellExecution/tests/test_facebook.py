import pytest


def test_facebook_chrome(chrome_driver):
    chrome_driver.get("https://www.facebook.com/")
    assert "Facebook – log in or sign up" in chrome_driver.title
