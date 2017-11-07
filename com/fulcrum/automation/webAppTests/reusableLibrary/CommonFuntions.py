
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)

class WebReusableFunctions:


    def __init__(self, driver, report):

        self.driver = driver
        self.report = report

    def splitArguments(self, arguments):
        splittedArgs = arguments.split('##')
        return splittedArgs

    def enterTextId(self, arguments):
        args = self.splitArguments(arguments)
        if len(args) == 2:
            self.driver.find_element_by_id(args[0]).send_keys(args[1])
            self.report.addTestStep('enterTextId', 'Enter Text by ID - ' + args[1], 'PASS')

    def enterTextName(self, name, value):

        self.driver.find_element_by_name(name).send_keys(value)
        self.report.addTestStep('enterTextName', 'Enter Text by NAME' + value, 'PASS')

    def clickElementId(self, argument):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, argument)))
        element.click()
        self.report.addTestStep('clickElementId', 'Click Element by ID', 'PASS')

    def clickElementName(self, name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.NAME, name)))
        element.click()
        self.report.addTestStep('clickElementName', 'Click Element by Name', 'PASS')

    def getUrl(self, arguments):
        args = self.splitArguments(arguments)
        self.driver.get(args[0])
        assert args[1] in self.driver.title
        self.report.addTestStep('getUrl','Web app with URL ' + args[0] + ' is launched successfully', 'PASS')

