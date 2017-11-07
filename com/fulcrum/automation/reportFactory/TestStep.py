import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class TestcaseStep:

    testStepCount = ''
    testStep = ''
    testStepDescription = ''
    testStepResult = ''
    testStepScreenshotName = ''

    def __init__(self,testStepCount, testStep, testStepDescription, testStepResult, testStepScreenshotName ):

        self.testStepCount = testStepCount
        self.testStep = testStep
        self.testStepDescription = testStepDescription
        self.testStepResult = testStepResult
        self.testStepScreenshotName = testStepScreenshotName




