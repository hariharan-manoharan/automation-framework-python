import os
from mobileAppTests.reusableLibrary.CommonFuntions import MobileReusableFunctions
from mobileAppTests.reusableLibrary.CustomFuntions import MobileCustomFunctions
from webAppTests.reusableLibrary.CommonFuntions import WebReusableFunctions
from webAppTests.reusableLibrary.CustomFuntions import WebCustomFunctions
from utils.ExcelUtils import ExcelTestDataAccess
from TestParameters import TestParameters

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class ExecutorService:

    def __init__(self,frameworkConfig, report, driver, testParameters):
        self.isMethodFound = False
        self.frameworkConfig = frameworkConfig
        self.report = report
        self.driver = driver
        self.testParameters = testParameters
        print 'ExecutorService Constructor executed'


    def getKeywords(self):

        testDataAccess = ExcelTestDataAccess()
        self.keywords = testDataAccess.getRowData('Keywords',self.testParameters.getTestcaseId())
        self.getArguments()

    def getArguments(self):

        testDataAccess = ExcelTestDataAccess()
        self.arguments = testDataAccess.getRowData('Keywords', self.testParameters.getTestcaseId()+'_ARGS')


    def executekeywords(self):
        self.report.startTest(self.testParameters.getTestDescription())
        for i in range(len(self.keywords)-1):

            currentKeyword = self.keywords['KEYWORD_'+str(i+1)]
            currentArguments = self.arguments['KEYWORD_'+str(i+1)]

            if 'Web App' == self.frameworkConfig.get('testing.type'):
                obj = WebReusableFunctions(self.driver, self.report)
                names = dir(WebReusableFunctions)
            elif 'Mobile App' == self.frameworkConfig.get('testing.type'):
                obj = MobileReusableFunctions()
                names = dir(MobileReusableFunctions)

            for name in names:
                attr = getattr(obj, name)
                if callable(attr) and name == currentKeyword and self.isMethodFound == False:
                    self.isMethodFound = True
                    attr(currentArguments)
                    if self.isMethodFound == True:
                        self.report.addTestStep('Keyword', currentKeyword + ' is executed sucessfully', 'PASS')
                        self.isMethodFound = False
                    else:
                        self.report.addTestStep('Keyword', currentKeyword + ' is executed sucessfully', 'PASS')