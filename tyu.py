import pytest
from selenium import webdriver

from base import BaseClass


# @pytest.mark.usefixtures("setup")
class test(BaseClass):

    def __init__(self,driver):
        self.driver=driver
    def testone(self):
        self.driver.find_element_by_xpath("/html/body/app-root/app-navbar/div/nav/ul/li[1]/a")
        print("success")
