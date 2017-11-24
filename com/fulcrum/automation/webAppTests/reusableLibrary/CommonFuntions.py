
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from ..pageObjectRepository.CommonObjects import CommonObjects
from selenium.webdriver.remote.webelement import WebElement

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class WebReusableFunctions(CommonObjects):

    element = WebElement

    def __init__(self, driver, report):
        CommonObjects.__init__(self)
        self.driver = driver
        self.report = report
        self.wait = WebDriverWait(self.driver, 20)

#    def split_arguments(self, arguments):
#        split_args = dict(argument.split('=') for argument in arguments.split(','))
#        return split_args

    '''
    Enter text in text box using id locator
    
        :param str id_locator
        :param str filed_name
        :param str text
    '''
    def enter_text_id(self, id_locator, field_name, text):
        self.driver.find_element_by_id(id_locator).send_keys(text)
        self.report.addTestStep('enter_text_id', text + ' is entered in field ' + field_name, 'PASS')

    '''
    Click element using id locator

        :param str id_locator 
        :param str object_name        
    '''
    def click_element_id(self, id_locator, object_name):
        self.element = self.wait.until(EC.element_to_be_clickable((By.ID, id_locator)))
        self.element.click()
        self.report.addTestStep('click_element_id', object_name + ' is clicked', 'PASS')

    '''
    Click element using xpath locator

        :param str xpath_locator 
        :param str object_name        
    '''
    def click_element_xpath(self, xpath_locator, object_name):
        if self.is_element_clickable('XPATH', xpath_locator):
            self.element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_locator)))
            if self.wait_until_element_is_present('XPATH',
                                                  '//div[@class=\'blocking-screen\']'):
                self.element.click()
                self.report.addTestStep('click_element_id', object_name + ' is clicked', 'PASS')
        else:
            self.report.addTestStep('click_element_id', object_name + ' is not clicked', 'FAIL')

    '''
    Enter text in text box using name locator

        :param str name_locator
        :param str field_name
        :param str text
    '''
    def enter_text_name(self, name_locator, field_name, text):
        self.driver.find_element_by_name(name_locator).send_keys(text)
        self.report.addTestStep('enter_text_name', text + ' is entered in field ' + field_name, 'PASS')

    '''
    Click element using name locator

        :param str name_locator 
        :param str object_name        
    '''
    def click_element_name(self, name_locator, object_name):
        self.element = self.wait.until(EC.element_to_be_clickable(name_locator))
        self.element.click()
        self.report.addTestStep('click_element_name', object_name + ' is clicked', 'PASS')

    '''
    Launch web application with given url and checks its title once the web page is loaded completely

        :param str url 
        :param str title        
    '''
    def get_url(self, url, title):
        self.driver.get(url)
        assert title in self.driver.title
        self.report.addTestStep('get_url', 'Web app with URL ' + url + ' is launched successfully', 'PASS')

    '''
    Asserts the current web page title 

        :param str title        
    '''
    def assert_title(self, title):
        assert title in self.driver.title
        self.report.addTestStep('assert_title', 'Title ' + title + ' is present', 'PASS')

    '''
    Clicks "Data Forms" link in CATS Home page

        :param nil        
    '''
    def click_data_forms_link(self):
        self.element = self.wait.until\
            (EC.element_to_be_clickable((By.XPATH, '// div[ @class =\'navbar-collapse collapse\'] / ul[1] / li[2] / a')))
        self.element.click()
        assert 'CATS CenterPoint: CenterPoint' in self.driver.title
        self.report.addTestStep('click_data_forms_link', 'Clicked Data Forms link', 'PASS')
    '''
    Clicks given data form

        :param str xpath 
        :param str data_form_name        
    '''
    def click_data_form(self, xpath, data_form_name):

        self.element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath.format(data_form_name))))
        self.element.click()

        self.element = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.xpath_btn.format('Search'))))
        if self.element.is_displayed():
            self.report.addTestStep('click_data_form', 'Clicked Data Form - ' + data_form_name, 'PASS')
        else:
            self.report.addTestStep('click_data_form',
                                    'Clicked Data Form - ' + data_form_name + '.'
                                    'Search screen is not displayed', 'FAIL')

    def click_button_search(self, xpath_search):

        if self.is_element_clickable('XPATH', xpath_search):
            self.element = self.driver.find_element_by_xpath(xpath_search)
            self.element.click()

            if self.is_element_present('XPATH', self.xpath_btn.format('Clear Grid')):
                self.report.addTestStep('click_button', 'Clicked button with text contains - Search', 'PASS')
            else:
                self.report.addTestStep('click_button',
                                        'Click button with text contains - Search. Results screen is not displayed', 'FAIL')
        else:
            self.report.addTestStep('click_button',
                                    'Not Clicked button with text contains - Search.', 'FAIL')

    def enter_text_by_xpath(self, xpath, field_name, text):

        is_present = self.is_element_present('XPATH', xpath.format(field_name))

        if is_present:
            self.element = self.driver.find_element_by_xpath(xpath.format(field_name))
            self.element.clear()
            self.element.send_keys(text)
            self.report.addTestStep('enter_text_by_xpath',
                                    text + ' is entered in field ' + field_name, 'PASS')
        else:
            self.report.addTestStep('enter_text_by_xpath',
                                    text + ' is not entered in field ' + field_name, 'FAIL')

    def get_text_xpath(self, xpath, field_name):

        is_present = self.is_element_present('XPATH', xpath.format(field_name))

        if is_present:
            text = self.driver.find_element_by_xpath(xpath.format(field_name)).text

            self.report.addTestStep('get_text_xpath',
                                    text + ' is returned from field ' + field_name, 'PASS')
            return text
        else:
            self.report.addTestStep('get_text_xpath',
                                    'None is returned. Field '+field_name+' is not present', 'FAIL')
            return None

    def is_element_present(self, by, locator):
        try:
            if by == 'XPATH':
                self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
                return True
            elif by == 'ID':
                self.wait.until(EC.presence_of_element_located((By.ID, locator)))
                return True
            elif by == 'NAME':
                self.wait.until(EC.presence_of_element_located((By.NAME, locator)))
                return True

            return False
        except NoSuchElementException:
            return False
        except WebDriverException:
            return False

    def is_element_clickable(self, by, locator):
        try:
            if by == 'XPATH':
                self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
                return True
            elif by == 'ID':
                self.wait.until(EC.element_to_be_clickable((By.ID, locator)))
                return True
            elif by == 'NAME':
                self.wait.until(EC.element_to_be_clickable((By.NAME, locator)))
                return True

            return False
        except NoSuchElementException:
            return False
        except WebDriverException:
            return False

    def wait_until_element_is_present(self, by, locator):
        try:
            if by == 'XPATH':
                self.wait.until_not(EC.presence_of_element_located((By.XPATH, locator)))
                return True
            elif by == 'ID':
                self.wait.until_not(EC.presence_of_element_located((By.ID, locator)))
                return True
            elif by == 'NAME':
                self.wait.until_not(EC.presence_of_element_located((By.NAME, locator)))
                return True

            return False
        except NoSuchElementException:
            return False
        except WebDriverException:
            return False

    def click_data_forms_folder(self, folder_name):
        self.element = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//div[contains(text(),\'' + folder_name + '\')]')))
        self.element.click()
        self.report.addTestStep('click_data_forms_folder', 'Clicked Data Forms folder - ' + folder_name, 'PASS')