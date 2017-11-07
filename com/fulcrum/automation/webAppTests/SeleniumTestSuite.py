from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from reusableLibrary.CommonFuntions import WebReusableFunctions
import os


fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class TestSuite1(WebReusableFunctions):

    def __init__(self,driver, report):
        WebReusableFunctions.__init__(self,driver, report)
        self.driver = driver
        print 'TestSuite1 constructor is executed...'

    def test1(self):
        self.startTest('Search Google scenario 1')
        self.driver.get('https://www.google.co.in')
        assert 'Google' in self.driver.title
        self.enterTextId('lst-ib', 'Selenium webdriver using Python')
        self.clickElementName('btnK')


    def test2(self):
        self.startTest('Search Google scenario 2')
        self.driver.get('https://www.google.co.in')
        assert 'Google' in self.driver.title
        self.enterTextId('lst-ib', 'Selenium webdriver using Java')
        self.clickElementName('btnK')











