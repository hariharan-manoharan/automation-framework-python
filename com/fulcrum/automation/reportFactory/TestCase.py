import os
from TestStep import TestcaseStep
import datetime

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class Testcase:

    testcaseCount = ''
    testcaseDescription = ''
    testcaseId = ''
    testcaseResult = ''
    startTestStartTime = ''
    startTestEndTime = ''
    totalTestExecutionTime = ''
    testSteps = []

    testStepCounter = 0
    testStepPassCounter = 0
    testStepFailCounter = 0
    testStepInfoCounter = 0

    failedTestSteps = []


    def __init__(self,testcaseCount,testcaseId,testcaseDescription):

        self.testcaseCount = testcaseCount
        self.testcaseDescription = testcaseDescription
        self.testcaseId = testcaseId
        self.testSteps = []
        self.failedTestSteps = []

    def getTestStepPassCount(self):
        return self.testStepPassCounter

    def getTestStepFailCount(self):
        return self.testStepFailCounter

    def setTescaseResult(self, testcaseResult):

        self.testcaseResult = testcaseResult

    def setTestStartTime(self):
        self.startTestStartTime = datetime.datetime.now()

    def setTestEndTime(self):
        self.startTestEndTime = datetime.datetime.now()

    def setTotalTestExecutionTime(self):
        self.totalTestExecutionTime = str(self.startTestEndTime - self.startTestStartTime)

    def collectFailedTestSteps(self, testStep, testDescription ):
        self.failedTestSteps.append(testStep+' : '+testDescription)

    def addTestStep(self, testStep, testDescription, status, screenshotName, timestamp):
        self.testStepCounter += 1
        if status == 'PASS':
            self.testStepPassCounter += 1
            self.testStepLocal = TestcaseStep(self.testStepCounter, testStep,testDescription, status, screenshotName, timestamp)
            self.testSteps.append(self.testStepLocal)
        elif status == 'FAIL':
            self.testStepFailCounter += 1
            self.testStepLocal = TestcaseStep(self.testStepCounter, testStep, testDescription, status, screenshotName, timestamp)
            self.testSteps.append(self.testStepLocal)

    def addTestStepInfo(self, testStep, testDescription, status,  timestamp, screenshotName=''):
        self.testStepCounter += 1
        if status == 'INFO':
            self.testStepInfoCounter += 1
            self.testStepLocal = TestcaseStep(self.testStepCounter, testStep, testDescription, status, screenshotName, timestamp)
            self.testSteps.append(self.testStepLocal)

