import os

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from com.fulcrum.automation.framework.reportFactory.StatusEnum import Status

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class MobileReusableFunctions:

    element = WebElement

    def __init__(self, driver, report):

        self.driver = driver
        self.report = report
        self.wait = WebDriverWait(self.driver, 30)

    def click_element_id(self, id_locator):
        self.element = self.wait.until(EC.element_to_be_clickable((By.ID, id_locator)))
        self.element.click()
        self.report.addTestStep('click_element_id', 'Click Element by ID', Status.PASS)

    def enter_text_id(self, id_locator, field_name, text):
        self.driver.find_element_by_id(id_locator).send_keys(text)
        self.report.addTestStep('enter_text_id', text + ' is entered in field ' + field_name, Status.PASS)

    def select_user_profile(self, profile):
        try:

            is_selected = False
            profile_bar_title = self.wait.until(EC.element_to_be_clickable((By.ID, 'action_bar_title')))
            if profile_bar_title.text == 'Profiles':
                elements = self.driver.find_elements_by_id('routine_name')

                for element in elements:
                    if element.text == profile:
                        element.click()
                        self.report.addTestStep('select_user_profile', 'Profile ' + profile + ' is selected', Status.PASS)
                        is_selected = True
                        break

            if not is_selected:
                self.report.addTestStep('select_user_profile', 'Profile ' + profile + ' is not selected', Status.FAIL)

        except TimeoutException as e:
            self.report.addTestStep('select_user_profile', 'Profile ' + profile + ' is not selected', 'FAIL')

    def select_routine_folder(self, routine_folder):
        try:

            is_selected = False
            routine_folder_bar_title = self.wait.until(EC.element_to_be_clickable((By.ID, 'action_bar_title')))
            if routine_folder_bar_title.text == 'Routines':
                elements = self.driver.find_elements_by_id('routine_name')
                for element in elements:
                    if element.text == routine_folder:
                        element.click()
                        self.report.addTestStep('select_routine_folder', 'Routine folder ' + routine_folder + ' is selected', Status.PASS)
                        is_selected = True
                        break

            if not is_selected:
                self.report.addTestStep('select_routine_folder', 'Routine folder ' + routine_folder + ' is not selected', Status.FAIL)

        except TimeoutException as e:
            self.report.addTestStep('select_user_profile', 'Routine folder ' + routine_folder + ' is not selected', Status.FAIL)

    def select_routine(self, routine_folder, routine):
        try:

            is_selected = False
            routine_folder_bar_title = self.wait.until(EC.element_to_be_clickable((By.ID, 'action_bar_title')))
            routine_bar_subtitle = self.wait.until(EC.element_to_be_clickable((By.ID, 'action_bar_subtitle')))
            if routine_folder_bar_title.text == routine_folder and routine_bar_subtitle.text == routine:
                elements = self.driver.find_elements_by_id('routine_name')
                for element in elements:
                    if element.text == routine:
                        element.click()
                        self.report.addTestStep('select_routine', 'Routine ' + routine + ' is selected', Status.PASS)
                        is_selected = True
                        break

            if not is_selected:
                self.report.addTestStep('select_routine', 'Routine ' + routine + ' is not selected', Status.FAIL)

        except TimeoutException as e:
            self.report.addTestStep('select_routine', 'Routine ' + routine + ' is not selected', Status.FAIL)