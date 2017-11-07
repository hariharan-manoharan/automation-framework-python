
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


    def enterTextId(self, id, value):

        self.driver.find_element_by_id(id).send_keys(value)
        self.report.addTestStep('enterTextId','Enter Text by ID - ' + value,'PASS')

    def enterTextName(self, name, value):

        self.driver.find_element_by_name(name).send_keys(value)
        self.report.addTestStep('enterTextName', 'Enter Text by NAME' + value, 'PASS')

    def clickElementId(self, id):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, id)))
        element.click()
        self.report.addTestStep('clickElementId', 'Click Element by ID', 'PASS')

    def clickElementName(self, name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.NAME, name)))
        element.click()
        self.report.addTestStep('clickElementName', 'Click Element by Name', 'PASS')

    def startTest(self, testDescription):
        self.report.startTest(testDescription)

