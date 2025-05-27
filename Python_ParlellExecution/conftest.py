import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService


@pytest.fixture
def chrome_driver():
    options = ChromeOptions()
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


print("Chrome driver fixture loaded")


@pytest.fixture
def edge_driver():
    options = EdgeOptions()
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()
