import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
