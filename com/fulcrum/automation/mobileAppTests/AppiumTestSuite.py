import os
from reusableLibrary.CommonFuntions import MobileReusableFunctions

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class TestSuite1(MobileReusableFunctions):


    def __init__(self,driver, report):
        MobileReusableFunctions.__init__(self,driver, report)
        self.driver = driver
        print 'TestSuite1 constructor is executed...'


    def test1(self):
        self.startTest('Appium Test 1')
        self.clickElementId('btn_connect')
