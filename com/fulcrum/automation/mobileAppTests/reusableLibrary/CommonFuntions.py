import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class MobileReusableFunctions:

    def __init__(self, driver, report):

        self.driver = driver
        self.report = report


    def clickElementId(self, id):

        self.driver.find_element_by_id(id).click()
        self.report.addTestStep('clickElementId', 'Click Element by ID', 'PASS')

    def startTest(self, testDescription):
        self.report.startTest(testDescription)
