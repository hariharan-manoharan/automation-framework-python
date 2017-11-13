import os
from TestStep import TestcaseStep

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class Testcase:

    testcaseCount = ''
    testcaseDescription = ''
    testcaseId = ''
    tescaseResult = ''
    testSteps = []

    testStepCounter = 0
    testStepPassCounter = 0
    testStepFailCounter = 0


    def __init__(self,testcaseCount,testcaseId,testcaseDescription):

        self.testcaseCount = testcaseCount
        self.testcaseDescription = testcaseDescription
        self.testcaseId = testcaseId
        self.testSteps = []

    def getTestStepPassCount(self):
        return self.testStepPassCounter

    def getTestStepFailCount(self):
        return self.testStepFailCounter


    def addTestStep(self, testStep, testDescription, status, screenshotName, timestamp):
        self.testStepCounter += 1
        if status == 'PASS':
            self.testStepPassCounter += 1
            testStepLocal = TestcaseStep(self.testStepCounter, testStep,testDescription, status, screenshotName, timestamp)
            self.testSteps.append(testStepLocal)
        elif status == 'FAIL':
            self.testStepFailCounter += 1
            testStepLocal = TestcaseStep(self.testStepCounter, testStep, testDescription, status, screenshotName, timestamp)
            self.testSteps.append(testStepLocal)