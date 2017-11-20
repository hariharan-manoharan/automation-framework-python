import os
from driverFactory import BrowserDriverFactory
from driverFactory import AndroidDriverFactory
from reportFactory.HtmlReportGenerator import HtmlReport
from utils.FrameworkConfig import FrameworkConfigParser
from utils.ExcelUtils import ExcelRunManagerAccess
from TestParameters import TestParameters
from Executor import ExecutorService
import errno
import datetime

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
        try:
            self.setExecutionStartTime()
            self.make_sure_path_exists('reports')
            self.getFrameworkConfig()
            if 'Web App' == self.frameworkConfig.get('testing.type'):
                self.createBrowserDriverObject()
            elif 'Mobile App' == self.frameworkConfig.get('testing.type'):
                self.createAndroidDriverObject()
            self.initializeReport()
            self. collectTestInstances()
            self.executeTest()
        except :
            print 'Execption occured in exeute method'
        finally:
            self.quitDriver()
            self.setExecutionEndTime()
            self.generateReport()



    def getFrameworkConfig(self):
        frameworkConfigurations = FrameworkConfigParser()
        self.frameworkConfig = frameworkConfigurations.readConfig()

    def collectTestInstances(self):
        runManagerAccess = ExcelRunManagerAccess()
        testinstances = runManagerAccess.getRunManagerInfo('RunManager')
        totalTestcasesToExecute = len(testinstances)
        self.totalTestInstanceToExecuteClean = []
        if totalTestcasesToExecute == 0:
            print 'No testcase is marked with Execute = Yes'
        else:
            for i in range(totalTestcasesToExecute):
                testParameters = TestParameters(testinstances[i]['TC_ID'],testinstances[i]['TEST_DESCRIPTION'],testinstances[i]['EXECUTE'])
                self.totalTestInstanceToExecuteClean.insert(i,testParameters)


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

        if len(self.totalTestInstanceToExecuteClean) !=0:
            for i in range(len(self.totalTestInstanceToExecuteClean)):
                self.totalTestInstanceToExecuteClean
                executor = ExecutorService(self.frameworkConfig, Base.htmlReport, Base.driver, self.totalTestInstanceToExecuteClean[i])
                executor.getKeywords()
                executor.executekeywords()

    def quitDriver(self):
        if 'Web App' == self.frameworkConfig.get('testing.type'):
            Base.driver.close()
        elif 'Mobile App' == self.frameworkConfig.get('testing.type'):
            #self.androidDriverFactory.killAppiumServerInstance()
            Base.driver.quit()


    def generateReport(self):
        totalTimeDelta = self.startExecutionEndTime - self.startExecutionStartTime
        Base.htmlReport.generateReport(str(totalTimeDelta))

        #hours = totalTimeDelta.seconds / 3600
        #minutes = totalTimeDelta.seconds / 60
        #seconds = totalTimeDelta.seconds

        #Base.htmlReport.generateReport(str(str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + ' secs'))



    def make_sure_path_exists(self, path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise


    def setExecutionStartTime(self):
        self.startExecutionStartTime = datetime.datetime.now()


    def setExecutionEndTime(self):
        self.startExecutionEndTime = datetime.datetime.now()

if __name__ == '__main__':
    Base().execute()





