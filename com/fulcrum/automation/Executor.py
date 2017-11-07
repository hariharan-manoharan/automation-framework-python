import os
from mobileAppTests.reusableLibrary.CommonFuntions import MobileReusableFunctions
from mobileAppTests.reusableLibrary.CustomFuntions import MobileCustomFunctions
from webAppTests.reusableLibrary.CommonFuntions import WebReusableFunctions
from webAppTests.reusableLibrary.CustomFuntions import WebCustomFunctions
from reportFactory.HtmlReportGenerator import HtmlReport

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class ExecutorService:

    def __init__(self,frameworkConfig, report, driver, testIntances):
        self.isMethodFound = False
        self.frameworkConfig = frameworkConfig
        self.report = report
        self.driver = driver
        self.testIntances = testIntances
        print 'ExecutorService Constructor executed'


    def executekeywords(self, currentKeyword):

        if 'Web App' == self.frameworkConfig.get('testing.type'):
            obj = WebReusableFunctions()
            names = dir(WebReusableFunctions)
        elif 'Mobile App' == self.frameworkConfig.get('testing.type'):
            obj = MobileReusableFunctions()
            names = dir(MobileReusableFunctions)

        for name in names:
            attr = getattr(obj, name)
            if callable(attr) and name == currentKeyword and self.isMethodFound == False:
                self.isMethodFound = True
                attr()

        if self.isMethodFound == True:
            self.report.addTestStep('Keyword',currentKeyword + ' is executed sucessfully','PASS')
        else:
            self.report.addTestStep('Keyword', currentKeyword + ' is executed sucessfully', 'PASS')







