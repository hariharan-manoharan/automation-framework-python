
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

    def split_arguments(self, arguments):
        split_args = dict(argument.split('=') for argument in arguments.split(','))
        return split_args

    def enter_text_id(self, args):
        args = self.split_arguments(args)

        if len(args) == 2:
            self.driver.find_element_by_id(args['id']).send_keys(args['text'])
            self.report.addTestStep('enterTextId', 'Enter Text by ID - ' + args['id'], 'PASS')

    def enter_text_name(self, args):
        args = self.split_arguments(args)

        self.driver.find_element_by_name(args['name']).send_keys(args['text'])
        self.report.addTestStep('enterTextName', 'Enter Text by NAME' + args['text'], 'PASS')

    def click_element_id(self, args):
        args = self.split_arguments(args)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, args['id'])))
        element.click()
        self.report.addTestStep('clickElementId', 'Click Element by ID', 'PASS')

    def click_element_name(self, args):
        args = self.split_arguments(args)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.NAME, args['name'])))
        element.click()
        self.report.addTestStep('clickElementName', 'Click Element by Name', 'PASS')

    def get_url(self, args):
        args = self.split_arguments(args)

        self.driver.get(args['url'])
        assert args['title'] in self.driver.title
        self.report.addTestStep('getUrl','Web app with URL ' + args['title'] + ' is launched successfully', 'PASS')

