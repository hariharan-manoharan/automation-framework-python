import os
from reports import Report
from TestStep import TestcaseStep
from TestCase import Testcase
from datetime import datetime

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class HtmlReport:

    reportDir = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    report = ''
    driver = ''
    testcaseCounter = 0
    testcases = []

    testcasePassCounter = 0
    testcaseFailCounter = 0

    currentTestcase = ''

    def __init__(self, driver):
        self.driver = driver
        self.report = Report(directory='reports/'+ 'Run-'+self.reportDir,searchpath='reportFactory/templates/',template_filename='Report Summary.html')
        self.report.jinja['title'] = 'Automation Test Summary'

    def startTest(self, testcaseDescription):
        self.testcaseCounter += 1
        self.currentTestcase = Testcase(self.testcaseCounter, testcaseDescription)
        self.testcases.append(self.currentTestcase)

    def addTestStep(self, testStep, testDescription, status):
        screenshotName = self.takeScreenshot()
        self.currentTestcase.addTestStep(testStep, testDescription, status, screenshotName+'.png')

    def generateReport(self):

        self.report.jinja['testcases'] = self.testcases
        self.report.jinja['testRunFolderName'] = self.reportDir
        self.report.create_report(onweb=True)

    def generateScreenshotName(self):
        screenshotName = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S%f'))
        return screenshotName

    def takeScreenshot(self):
        screenshotName = self.generateScreenshotName()
        self.driver.save_screenshot('reports/'+'Run-'+self.reportDir+'/images/'+screenshotName+'.png')
        return screenshotName







