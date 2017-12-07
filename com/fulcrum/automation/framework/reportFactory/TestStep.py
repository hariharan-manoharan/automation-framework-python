import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class TestcaseStep:

    testStepCount = ''
    testStep = ''
    testStepDescription = ''
    testStepResult = ''
    testStepScreenshotName = ''
    testtTimestamp = ''

    def __init__(self,testStepCount, testStep, testStepDescription, testStepResult, testStepScreenshotName, testtTimestamp ):

        self.testStepCount = testStepCount
        self.testStep = testStep
        self.testStepDescription = testStepDescription
        self.testStepResult = testStepResult
        self.testStepScreenshotName = testStepScreenshotName
        self.testtTimestamp = testtTimestamp




