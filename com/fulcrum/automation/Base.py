import os
from driverFactory import BrowserDriverFactory
from driverFactory import AndroidDriverFactory
from webAppTests import SeleniumTestSuite
from mobileAppTests import AppiumTestSuite
from reportFactory.HtmlReportGenerator import HtmlReport
from utils.FrameworkConfig import FrameworkConfigParser
import Executor

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class Base:


    driver = ''
    htmlReport = ''
    browserDriverFactory = ''
    androidDriverFactory = ''
    frameworkConfig = {}


    def __init__(self):
        print 'Base class constructor executed...'

    def execute(self):
        self.getFrameworkConfig()
        if 'Web App' == self.frameworkConfig.get('testing.type'):
            self.createBrowserDriverObject()
        elif 'Mobile App' == self.frameworkConfig.get('testing.type'):
            self.createAndroidDriverObject()
        self.initializeReport()
        self. collectTestInstances()
        self.executeTest()
        self.quitDriver()
        self.generateReport()

    def getFrameworkConfig(self):
        frameworkConfigurations = FrameworkConfigParser()
        self.frameworkConfig = frameworkConfigurations.readConfig()

    def collectTestInstances(self):
        pass


    def initializeReport(self):
        Base.htmlReport = HtmlReport(Base.driver)

    def createBrowserDriverObject(self):

        self.browserDriverFactory = BrowserDriverFactory.DriverScript(self.frameworkConfig)
        self.browserDriverFactory.setDriver(self.frameworkConfig.get('browser'))
        Base.driver = self.browserDriverFactory.getDriver()

    def createAndroidDriverObject(self):

        self.androidDriverFactory = AndroidDriverFactory.DriverScript(self.frameworkConfig.get('remote.port'), self.frameworkConfig)
        #self.androidDriverFactory.startAppiumServerInstance()
        self.androidDriverFactory.setDriver()
        Base.driver = self.androidDriverFactory.getDriver()

    def executeTest(self):
        executor = Executor(self.frameworkConfig, Base.htmlReport, Base.driver, )


    def quitDriver(self):
        if 'Web App' == self.frameworkConfig.get('testing.type'):
            Base.driver.close()
        elif 'Mobile App' == self.frameworkConfig.get('testing.type'):
            #self.androidDriverFactory.killAppiumServerInstance()
            Base.driver.quit()


    def generateReport(self):
        Base.htmlReport.generateReport()

if __name__ == '__main__':
    Base().execute()





