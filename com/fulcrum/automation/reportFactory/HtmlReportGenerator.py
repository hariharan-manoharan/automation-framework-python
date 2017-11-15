import os
from reports import Report
from TestStep import TestcaseStep
from TestCase import Testcase
from datetime import datetime
import errno
import shutil
from jinja2 import Environment, FileSystemLoader

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class HtmlReport:

    reportDir = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    dashboard_report = ''
    testcase_report = ''
    driver = ''
    testcaseCounter = 0
    testcases = []

    testcasePassCounter = 0
    testcaseFailCounter = 0

    failedTestCases = []

    currentTestcase = ''

    def __init__(self, driver):
        self.driver = driver
        self.copyReportTemplates()
        self.make_sure_path_exists('reports/'+ 'Run-'+self.reportDir)
        self.make_sure_path_exists('reports/' + 'Run-' + self.reportDir+'/images')


    def startTest(self, testcaseId, testcaseDescription):
        self.testcaseCounter += 1
        self.currentTestcase = Testcase(self.testcaseCounter, testcaseId, testcaseDescription)
        self.currentTestcase.setTestStartTime()
        self.testcases.append(self.currentTestcase)

    def endTest(self):
        self.currentTestcase.setTestEndTime()
        self.currentTestcase.setTotalTestExecutionTime()
        if self.currentTestcase.getTestStepFailCount() > 0:
            self.testcaseFailCounter += 1
            self.currentTestcase.setTescaseResult('FAIL')
            self.failedTestCases.append(self.currentTestcase)
        else:
            self.currentTestcase.setTescaseResult('PASS')
            self.testcasePassCounter += 1

    def addTestStep(self, testStep, testDescription, status):

        if status == 'PASS' or status == 'FAIL':
            screenshotName = self.takeScreenshot()
            self.currentTestcase.addTestStep(testStep, testDescription, status, screenshotName+'.png', str(datetime.now().strftime('%H:%M:%S')))
        elif status == 'INFO':
            self.currentTestcase.addTestStepInfo(testStep, testDescription, status, str(datetime.now().strftime('%H:%M:%S')))


        if status == 'FAIL':
            self.currentTestcase.collectFailedTestSteps(testStep, testDescription)


    def generateReport(self, totalExecutionTime):

        j2_env = Environment(loader=FileSystemLoader(fileDir),
                             trim_blocks=True)

        output_from_parsed_template_dashboard = j2_env.get_template('reports/'+'Run-'+self.reportDir+'/templates/dashboard.html').render(
        totaltests = self.testcaseCounter,
        testsPassed = self.testcasePassCounter,
        testsFailed = self.testcaseFailCounter,
        totalExecutionTime = totalExecutionTime,
        testcases= self.testcases,
        testRunFolderName = self.reportDir,
        failedTestCases = self.failedTestCases
        )

        with open('reports/'+'Run-'+self.reportDir+'/dashboard.html', "w+") as file:
            file.write(output_from_parsed_template_dashboard)


        for testcase in self.testcases:
            output_from_parsed_template_testcase = j2_env.get_template('reports/'+'Run-'+self.reportDir+'/templates/testcase.html').render(
            testcases=self.testcases,
            testcase= testcase,
            testSteps = testcase.testSteps,
            testRunFolderName = self.reportDir
            )

            with open('reports/' + 'Run-' + self.reportDir + '/'+testcase.testcaseId+'.html', "w+") as file:
                file.write(output_from_parsed_template_testcase)

    def generateReportImmediateFlush(self):

        j2_env = Environment(loader=FileSystemLoader(fileDir),
                             trim_blocks=True)

        output_from_parsed_template_dashboard = j2_env.get_template('reports/'+'Run-'+self.reportDir+'/templates/dashboard.html').render(
        totaltests = self.testcaseCounter,
        testsPassed = self.testcasePassCounter,
        testsFailed = self.testcaseFailCounter,
        totalExecutionTime = 'Execution in progress',
        testcases= self.testcases,
        testRunFolderName = self.reportDir,
        failedTestCases = self.failedTestCases
        )

        with open('reports/'+'Run-'+self.reportDir+'/dashboard.html', "w+") as file:
            file.write(output_from_parsed_template_dashboard)


        for testcase in self.testcases:
            output_from_parsed_template_testcase = j2_env.get_template('reports/'+'Run-'+self.reportDir+'/templates/testcase.html').render(
            testcases=self.testcases,
            testcase= testcase,
            testSteps = testcase.testSteps,
            testRunFolderName = self.reportDir
            )

            with open('reports/' + 'Run-' + self.reportDir + '/'+testcase.testcaseId+'.html', "w+") as file:
                file.write(output_from_parsed_template_testcase)


    def generateScreenshotName(self):
        screenshotName = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S%f'))
        return screenshotName

    def takeScreenshot(self):
        screenshotName = self.generateScreenshotName()
        self.driver.save_screenshot('reports/'+'Run-'+self.reportDir+'/images/'+screenshotName+'.png')
        return screenshotName

    def make_sure_path_exists(self, path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def copyReportTemplates(self):

        source = 'reportFactory/templates'
        destination = 'reports/'+'Run-'+self.reportDir

        try:
            shutil.copytree(source, destination)
        except OSError as exc:  # python >2.5
            if exc.errno == errno.ENOTDIR:
                shutil.copy(source, destination)
            else:
                raise









