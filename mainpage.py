from _pytest import unittest
from selenium import webdriver
import unittest

from login import Login


class test:

    def dri(self):
        self.driver = webdriver.Chrome()

    def test_login(self):

        self.driver.get("https://www.facebook.com/")

        login1 = Login(self.driver)
        login1.username("9482434074")
        login1.password("Rohith@9482")
        login1.login()


test1 = test()
test1.dri()
test1.test_login()
