import os
from TestStep import TestcaseStep

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class Testcase:

    testcaseCount = ''
    testcaseDescription = ''
    tescaseResult = ''
    testSteps = []

    testStepCounter = 0
    testStepPassCounter = 0
    testStepFailCounter = 0


    def __init__(self,testcaseCount,testcaseDescription):

        self.testcaseCount = testcaseCount
        self.testcaseDescription = testcaseDescription
        self.testSteps = []


    def addTestStep(self, testStep, testDescription, status, screenshotName):
        self.testStepCounter += 1
        if status == 'PASS':
            self.testStepPassCounter += 1
            testStepLocal = TestcaseStep(self.testStepCounter, testStep,testDescription, status, screenshotName)
            self.testSteps.append(testStepLocal)
        elif status == 'FAIL':
            self.testStepFailCounter += 1
            testStepLocal = TestcaseStep(self.testStepCounter, testStep, testDescription, status, screenshotName)
            self.testSteps.append(testStepLocal)